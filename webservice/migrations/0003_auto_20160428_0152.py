# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0002_todo_reminder_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=1, to='webservice.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='reminder_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 28, 1, 52, 45, 19127)),
        ),
    ]
