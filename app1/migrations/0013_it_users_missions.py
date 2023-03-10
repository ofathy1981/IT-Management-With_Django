# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-11 08:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0012_auto_20180708_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='it_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='missions',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=120, primary_key=True, serialize=False)),
                ('mission1', models.TextField(max_length=120, verbose_name='المهامه الاولى')),
                ('mission2', models.TextField(max_length=120, verbose_name='المهامه الثانيه')),
                ('mission3', models.TextField(max_length=120, verbose_name='المهامه الثالثه')),
                ('mission4', models.TextField(max_length=120, verbose_name='المهامه الراپعه')),
                ('mission5', models.TextField(max_length=120, verbose_name='المهامه الخامسه')),
                ('mission6', models.TextField(max_length=120, verbose_name='المهامه السادسه')),
                ('mission7', models.TextField(max_length=120, verbose_name='المهامه الساپعه')),
                ('mission8', models.TextField(max_length=120, verbose_name='المهامه الثامنه')),
                ('mission9', models.TextField(max_length=120, verbose_name='المهامه التاسعه')),
                ('mission10', models.TextField(max_length=120, verbose_name='المهامه العاشره')),
                ('place', models.CharField(blank=True, choices=[('داخل الشرگه', 'داخل الشرگه'), ('چهه اخرى', 'چهه اخرى')], default='داخل الشرگه', max_length=120, verbose_name='المگان ')),
                ('bransh', models.CharField(choices=[('الفواله', 'الفواله'), ('المهندسيين', 'المهندسيين'), ('جاردن سيتى', 'جاردن سيتى'), ('سيتى بنك', 'سيتى بنك'), ('قصر النيل', 'قصر النيل'), ('التوفيقيه', 'التوفيقيه')], max_length=120, null=True, verbose_name='اسم الفرع')),
                ('out_premisis', models.CharField(blank=True, max_length=120, verbose_name='چهة خارچ الشرگه')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('ip', models.CharField(max_length=120, null=True)),
                ('it_name', models.ForeignKey(blank=True, max_length=120, on_delete=django.db.models.deletion.CASCADE, to='app1.it_users', verbose_name='الاسم')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
