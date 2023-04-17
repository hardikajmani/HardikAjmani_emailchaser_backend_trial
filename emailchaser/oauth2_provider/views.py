from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from core.models import ConnectedEmail
from django.shortcuts import redirect, render
from django.conf import settings
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
import datetime
import pytz
import requests
import json
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.azure.views import AzureOAuth2Adapter
from allauth.socialaccount.models import SocialAccount, SocialToken
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.decorators import api_view


@api_view(["GET"])
def google_after_login_callback(request):
    social_account = SocialAccount.objects.get(provider='Google')
    social_token = SocialToken.objects.get(account=social_account)
    access_token = social_token.token

    # create ConnectedEmail object and save it to database
    ConnectedEmail.objects.create(
        user=request.user,
        provider='google',
        access_token=access_token,
        refresh_token=None  # refresh token is not available for Google OAuth2
    )
    # print(request)
    # redirect to home screen
    return redirect('home')
    # if token:
    #     social_account = adapter.get_provider().sociallogin_from_token(
    #         token, request=request
    #     )
    #     email = social_account.user.email
    #     ConnectedEmail.objects.create(provider="google", email=email, token=token)
    #     return redirect(reverse("home"))
    # else:
    #     return redirect(reverse("login"))


@api_view(["GET"])
def outlook_oauth2_callback(request):
    adapter = AzureOAuth2Adapter(
        client_id=OUTLOOK_CLIENT_ID, secret_key=OUTLOOK_CLIENT_SECRET
    )
    client = OAuth2Client(request)
    token = adapter.parse_token(request, client)
    if token:
        social_account = adapter.get_provider().sociallogin_from_token(
            token, request=request
        )
        email = social_account.user.email
        ConnectedEmail.objects.create(provider="outlook", email=email, token=token)
        return redirect(reverse("home"))
    else:
        return redirect(reverse("login"))


class GoogleOAuth2View(View):
    @method_decorator(login_required)
    def get(self, request):
        flow = Flow.from_client_config(
            settings.GOOGLE_OAUTH2_CLIENT_CONFIG,
            scopes=["https://www.googleapis.com/auth/gmail.compose"],
        )
        flow.redirect_uri = request.build_absolute_uri(
            reverse("google-oauth2-callback")
        )
        authorization_url, state = flow.authorization_url(
            access_type="offline", include_granted_scopes="true"
        )
        request.session["google_oauth2_state"] = state
        request.session["google_oauth2_user_id"] = request.user.id
        return HttpResponseRedirect(authorization_url)


class GoogleOAuth2CallbackView(View):
    @method_decorator(login_required)
    def get(self, request):
        state = request.session.get("google_oauth2_state")
        user_id = request.session.get("google_oauth2_user_id")
        if not state or not user_id:
            return HttpResponseBadRequest("Missing state or user ID in session.")
        flow = Flow.from_client_config(
            settings.GOOGLE_OAUTH2_CLIENT_CONFIG,
            scopes=["https://www.googleapis.com/auth/gmail.compose"],
            state=state,
        )
        flow.redirect_uri = request.build_absolute_uri(
            reverse("google-oauth2-callback")
        )
        authorization_response = request.build_absolute_uri()
        flow.fetch_token(authorization_response=authorization_response)
        credentials = flow.credentials
        connected_email, _ = ConnectedEmail.objects.get_or_create(
            user_id=user_id, email_address=credentials.id_token["email"]
        )
        connected_email.access_token = credentials.token
        connected_email.refresh_token = credentials.refresh_token
        connected_email.expires_at = credentials.expiry
        connected_email.save()
        return HttpResponseRedirect(reverse("home"))
