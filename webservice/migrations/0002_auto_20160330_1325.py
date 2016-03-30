# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('UUID', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=200)),
                ('due_datetime', models.DateTimeField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='UUID',
            field=models.CharField(max_length=36, serialize=False, primary_key=True),
        ),
    ]
