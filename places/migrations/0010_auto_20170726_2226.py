# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-26 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20170725_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='ionic_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='push_token',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
