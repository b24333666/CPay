# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='alocation',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]