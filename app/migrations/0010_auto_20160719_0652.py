# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-19 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160717_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predefinedservice',
            name='description',
            field=models.TextField(default='No description available.'),
        ),
    ]
