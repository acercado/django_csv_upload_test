# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151105_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loyaltycodes2',
            name='loyalty_point',
        ),
    ]
