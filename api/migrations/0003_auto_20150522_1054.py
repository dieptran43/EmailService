# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150121_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_email', models.CharField(max_length=100)),
                ('from_name', models.CharField(max_length=30)),
                ('reply_to', models.CharField(max_length=30)),
                ('important', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=100)),
                ('html', models.CharField(max_length=40000)),
                ('email_status', models.IntegerField(choices=[(1, b'Unknown'), (2, b'Email Sent'), (3, b'Failed to send email')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailAttachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20)),
                ('file_name', models.CharField(max_length=60)),
                ('attachment', models.FileField(upload_to=b'/tmp/storage/imagepath')),
                ('email', models.ForeignKey(to='api.Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailBcc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_address', models.EmailField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email', models.ForeignKey(to='api.Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailImagePath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20)),
                ('file_name', models.CharField(max_length=60)),
                ('attachment', models.FileField(upload_to=b'/tmp/storage/imagepath')),
                ('email', models.ForeignKey(to='api.Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailRecipients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_address', models.EmailField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email', models.ForeignKey(to='api.Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='emailmessage',
            name='user',
        ),
        migrations.DeleteModel(
            name='EmailMessage',
        ),
    ]
