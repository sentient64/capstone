# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-05 08:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20160905_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 5, 8, 54, 54, 410952)),
        ),
    ]
