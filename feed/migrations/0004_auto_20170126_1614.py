# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20170126_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='contents',
            new_name='content',
        ),
    ]
