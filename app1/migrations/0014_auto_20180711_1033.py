# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-11 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_it_users_missions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missions',
            name='id',
            field=models.CharField(max_length=120, primary_key=True, serialize=False),
        ),
    ]
