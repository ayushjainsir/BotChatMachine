# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20170411_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='botrespond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default=b'What?', max_length=100000000)),
                ('answere', models.CharField(default=b'yes.', max_length=10000000)),
            ],
        ),
    ]