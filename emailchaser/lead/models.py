from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lead(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    company = models.CharField(max_length=255)
    website = models.URLField()
    registered_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.email_address
