# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-21 21:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211222_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 22, 0, 39, 19, 827349), verbose_name='Опубликована'),
        ),
    ]
