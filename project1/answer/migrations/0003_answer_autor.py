# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 10:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('answer', '0002_auto_20171122_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
