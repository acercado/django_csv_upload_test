# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_loyaltycodes2_loyalty_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='loyaltycodes2',
            name='variant',
            field=models.CharField(choices=[('JDTW & JDTH', 'JDTW & JDTH'), ('Gentleman Jack', 'Gentleman Jack'), ('Single Barrel', 'Single Barrels')], default='JDTW & JDTH', max_length=20),
        ),
    ]
