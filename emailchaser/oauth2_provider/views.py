from django.conf import settings
from django.contrib.auth.decorators import login_required
from core.models import ConnectedEmail
from django.conf import settings
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from django.shortcuts import redirect


@login_required
def google_send_email(request):
    # TODO
    pass
