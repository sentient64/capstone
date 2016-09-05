# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-05 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_specialservice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialservice',
            name='service',
        ),
        migrations.AddField(
            model_name='service',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='SpecialService',
        ),
    ]