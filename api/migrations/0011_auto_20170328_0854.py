# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-28 05:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20170326_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='createdAt',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='createdAt',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='createdAt',
            new_name='created_at',
        ),
    ]
