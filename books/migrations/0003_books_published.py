# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-15 09:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180614_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='published',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
