# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 22:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0002_auto_20170323_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='places', to=settings.AUTH_USER_MODEL),
        ),
    ]
