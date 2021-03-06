# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 05:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upype', models.CharField(choices=[('per', 'Pre-Sales'), ('aft', 'After-Sales')], default='none', max_length=20)),
                ('datetime', models.DateTimeField()),
                ('client', models.CharField(blank=True, max_length=50)),
                ('project', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
