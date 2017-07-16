# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-19 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20170517_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='places.Place'),
        ),
    ]
