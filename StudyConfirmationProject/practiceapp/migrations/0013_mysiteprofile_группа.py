# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practiceapp', '0012_auto_20160819_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysiteprofile',
            name='Группа',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
