# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-02 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20160829_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='providerprofile',
            old_name='bio',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='providerprofile',
            old_name='address',
            new_name='street_address',
        ),
        migrations.AddField(
            model_name='providerprofile',
            name='area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='providerprofile',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='providerprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='providerprofile',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
