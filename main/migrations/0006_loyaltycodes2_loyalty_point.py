# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_loyaltycodes2_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='loyaltycodes2',
            name='loyalty_point',
            field=models.IntegerField(default=0),
        ),
    ]
