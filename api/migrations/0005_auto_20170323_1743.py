# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-23 15:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170323_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medal',
            name='user',
        ),
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(1)]),
        ),
    ]