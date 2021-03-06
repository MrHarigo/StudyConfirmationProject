# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-23 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practiceapp', '0017_auto_20160820_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=10)),
                ('surname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=10)),
                ('fathername', models.CharField(max_length=20)),
                ('amount', models.IntegerField(default=0)),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practiceapp.Certificate')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='certificate',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
