from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from core.models import ConnectedEmail
from django.contrib.auth.models import User

class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        print("_______________user------------")
        print(user.__dict__)
        user = super().save_user(request, user, form, False)
        # if commit:
        user.save()
        return user
    def get_login_redirect_url(self, request):
        return "/"


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        connected_email = ConnectedEmail.create_from_social_account(sociallogin)
        print(request)
        print(sociallogin.serialize())
        print(data)        
        try:
            user = User.objects.get(username = sociallogin.user.username)
        except Exception as e:
            print(sociallogin.user.__dict__)
            sociallogin.user.save()
            connected_email.user = sociallogin.user
        else:
            connected_email.user = user
        connected_email.save()
