# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 20:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20170409_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='fromuser_id',
            field=models.ForeignKey(db_column='fromuser_id', on_delete=django.db.models.deletion.CASCADE, related_name='fromuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='touser_id',
            field=models.ForeignKey(db_column='touser_id', on_delete=django.db.models.deletion.CASCADE, related_name='touser', to=settings.AUTH_USER_MODEL),
        ),
    ]