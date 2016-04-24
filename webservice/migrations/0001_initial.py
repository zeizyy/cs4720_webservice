# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
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
        migrations.CreateModel(
            name='Event',
            fields=[
                ('UUID', models.CharField(max_length=60, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('weekday', models.IntegerField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=24)),
                ('password', models.CharField(max_length=96)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to='webservice.User'),
        ),
    ]
