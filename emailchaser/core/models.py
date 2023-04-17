from django.db import models
from django.contrib.auth.models import User
import datetime


class ConnectedEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    provider = models.CharField(max_length=255)  # 'google' or 'outlook'
    token = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    @classmethod
    def create_from_social_account(cls, user, sociallogin):
        return cls(
            user=user,
            email=sociallogin.account.extra_data.get("email", None),
            provider=sociallogin.account.provider,
            token=sociallogin.token.token,
            refresh_token=None,
            expires_at=sociallogin.token.expires_at,
        )

    @classmethod
    def update(self, sociallogin):
        self.token = sociallogin.token.token
        self.refresh_token = None
        self.expires_at = sociallogin.token.expires_at
        self.save()

    def __str__(self):
        return self.email
