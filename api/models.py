from django.db import models
from django.contrib.auth.models import User

class EmailMessage(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 250)
