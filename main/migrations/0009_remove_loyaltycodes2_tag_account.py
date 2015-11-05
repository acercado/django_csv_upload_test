# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151105_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loyaltycodes2',
            name='tag_account',
        ),
    ]
