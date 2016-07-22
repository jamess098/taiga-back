# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-22 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0012_auto_20160614_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='epic_order',
            field=models.IntegerField(default=10000, verbose_name='epic order'),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='kanban_order',
            field=models.IntegerField(default=10000, verbose_name='kanban order'),
        ),
    ]
