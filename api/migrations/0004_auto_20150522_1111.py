# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150522_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailattachment',
            name='created',
            field=models.DateTimeField(default=datetime.date(2015, 5, 22), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailattachment',
            name='updated',
            field=models.DateTimeField(default=datetime.date(2015, 5, 22), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailimagepath',
            name='created',
            field=models.DateTimeField(default=datetime.date(2015, 5, 22), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailimagepath',
            name='updated',
            field=models.DateTimeField(default=datetime.date(2015, 5, 22), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailattachment',
            name='attachment',
            field=models.FileField(upload_to=b'/tmp/storage/attachments'),
        ),
    ]
