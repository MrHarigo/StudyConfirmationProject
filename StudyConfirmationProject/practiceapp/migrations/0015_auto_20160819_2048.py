# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practiceapp', '0014_auto_20160819_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mysiteprofile',
            old_name='Группа',
            new_name='group',
        ),
    ]
