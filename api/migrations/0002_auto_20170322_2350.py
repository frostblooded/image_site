# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-22 21:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='creator',
        ),
    ]
