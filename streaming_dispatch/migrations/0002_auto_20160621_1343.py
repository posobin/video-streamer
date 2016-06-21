# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 13:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_dispatch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
