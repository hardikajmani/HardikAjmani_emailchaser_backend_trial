from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from core.models import ConnectedEmail
from django.contrib.auth.models import User


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return "/"


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        try:
            connected_email = ConnectedEmail.objects.get(
                email=sociallogin.account.extra_data.get("email", "")
            )
            connected_email.update(sociallogin)
        except Exception as e:
            print(e)
            print("Connected Email not found")

        return user

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        try:
            connected_email = ConnectedEmail.objects.get(
                email=sociallogin.account.extra_data.get("email", "")
            )
            connected_email.update(sociallogin)
        except Exception as e:
            print("Connected Email not found")
            connected_email = ConnectedEmail.create_from_social_account(
                user, sociallogin
            )
            connected_email.save()
            print("saved")

        return user
