# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-05 08:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_auto_20160905_0856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='created_date',
            new_name='created',
        ),
    ]
