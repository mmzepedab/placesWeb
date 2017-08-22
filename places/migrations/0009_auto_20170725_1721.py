# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-25 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20170722_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='push_token',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appuser',
            name='facebook_id',
            field=models.CharField(error_messages={'unique': 'This User Already Registered'}, max_length=200, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='placesubscriber',
            unique_together=set([('place', 'user')]),
        ),
    ]