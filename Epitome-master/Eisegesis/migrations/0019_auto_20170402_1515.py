# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-02 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Eisegesis', '0018_auto_20170402_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposals',
            name='P_CREATION',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 2, 12, 15, 14, 557743, tzinfo=utc)),
        ),
    ]
