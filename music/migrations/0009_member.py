# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-08 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_delete_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('photo', models.FileField(max_length=1000, upload_to='')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
