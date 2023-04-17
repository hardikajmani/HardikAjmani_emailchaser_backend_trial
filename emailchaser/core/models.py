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
    def create_from_social_account(cls, sociallogin):
        return cls(
            user=sociallogin.user,
            email=sociallogin.account.extra_data.get("email", None),
            provider=sociallogin.account.provider,
            token=sociallogin.account.extra_data.get("at_hash", None),
            refresh_token=None,
            expires_at=datetime.datetime.fromtimestamp(
                sociallogin.account.extra_data.get("exp", 0)
            ),
        )

    def __str__(self):
        return self.email
