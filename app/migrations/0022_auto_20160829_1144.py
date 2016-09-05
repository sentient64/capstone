# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-29 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providerprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='providerprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='providerprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='providerprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='providers'),
        ),
        migrations.AlterField(
            model_name='providerprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
