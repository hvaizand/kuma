# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-06 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_squashed_0036_update_locales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentzone',
            name='document',
        ),
        migrations.RemoveField(
            model_name='document',
            name='zone_subnav_local_html',
        ),
        migrations.DeleteModel(
            name='DocumentZone',
        ),
    ]
