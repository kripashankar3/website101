# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-08 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_auto_20171208_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='track',
            new_name='audio',
        ),
    ]
