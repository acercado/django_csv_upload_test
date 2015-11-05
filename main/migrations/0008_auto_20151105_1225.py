# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151105_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loyaltycodes2',
            name='tag_account',
            field=models.ForeignKey(to='main.Account'),
        ),
    ]
