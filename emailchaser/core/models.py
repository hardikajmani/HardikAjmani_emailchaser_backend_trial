from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email


class ConnectedEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_address = models.EmailField()
    provider = models.CharField(max_length=255) # 'google' or 'outlook'
    access_token = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email_address
