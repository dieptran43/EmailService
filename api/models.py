from django.db import models
from emailservice.settings import UPLOAD_ATTACHMENT_PATH, UPLOAD_IMAGE_PATH
from django.db.models import Lookup
from django.db.models.fields import Field

class Email(models.Model):
    Unknown = 1
    Sent = 2
    Failed = 3
    EMAIL_STATUS = (
        (Unknown, 'Unknown'),
        (Sent, 'Email Sent'),
        (Failed, 'Failed to send email'),
    )
    from_email = models.CharField(max_length=100)
    from_name = models.CharField(max_length=30)
    reply_to = models.CharField(max_length=30)
    important = models.BooleanField(default=False)
    subject = models.CharField(max_length=100)
    html = models.CharField(max_length=40000)
    email_status = models.IntegerField(choices=EMAIL_STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class EmailRecipients(models.Model):
    email_address = models.EmailField()
    email = models.ForeignKey(Email)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class EmailBcc(models.Model):
    email_address = models.EmailField()
    email = models.ForeignKey(Email)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class EmailAttachment(models.Model):
    type = models.CharField(max_length=20)
    file_name = models.CharField(max_length=60)
    email = models.ForeignKey(Email)
    attachment = models.FileField(upload_to=UPLOAD_ATTACHMENT_PATH)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class EmailImagePath(models.Model):
    type = models.CharField(max_length=20)
    file_name = models.CharField(max_length=60)
    email = models.ForeignKey(Email)
    attachment = models.FileField(upload_to=UPLOAD_IMAGE_PATH)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




