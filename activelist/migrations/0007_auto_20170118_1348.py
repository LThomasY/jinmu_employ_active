# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activelist', '0006_auto_20170113_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activelist',
            name='expendtime',
            field=models.IntegerField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='clientl',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectl',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
