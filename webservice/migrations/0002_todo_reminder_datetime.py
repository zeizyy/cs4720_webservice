# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='reminder_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 28, 1, 36, 7, 422573)),
        ),
    ]
