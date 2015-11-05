# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_loyaltycodes2_tag_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='loyaltycodes2',
            name='premise',
            field=models.CharField(choices=[('On-Premise', 'On-Premise'), ('Off-Premise', 'Off-Premise')], max_length=20, default='On-Premise'),
        ),
    ]
