# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-23 13:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('practiceapp', '0018_auto_20160823_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 23, 13, 22, 40, 103594, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
