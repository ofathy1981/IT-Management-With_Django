# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-11 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_auto_20180711_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missions',
            name='id',
            field=models.CharField(default=uuid.uuid4, max_length=120, primary_key=True, serialize=False),
        ),
    ]