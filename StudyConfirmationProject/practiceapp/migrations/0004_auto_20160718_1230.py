# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practiceapp', '0003_auto_20160714_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='cer_amount',
            new_name='amount',
        ),
    ]
