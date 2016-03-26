# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0002_auto_20160325_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticator',
            fields=[
                ('authenticator', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
