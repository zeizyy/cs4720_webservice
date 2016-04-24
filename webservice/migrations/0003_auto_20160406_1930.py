# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0002_auto_20160330_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='weekday',
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
