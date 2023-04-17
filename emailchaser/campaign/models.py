from django.db import models
from django.contrib.auth.models import User
from core.models import ConnectedEmail
from lead.models import Lead


# Create your models here.
class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    message = models.TextField()
    registerd_user = models.ForeignKey(User, on_delete=models.CASCADE)
    leads = models.ManyToManyField(Lead)
    schedule_time = models.DateTimeField()
