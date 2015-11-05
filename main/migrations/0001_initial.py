# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loyaltycodes2',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('variant', models.CharField(default='JDTW & JDTH', max_length=20, choices=[('JDTW & JDTH', 'JDTW & JDTH'), ('Gentleman Jack', 'Gentleman Jack'), ('Single Barrel', 'Single Barrels')])),
                ('volume', models.CharField(default='700mL', max_length=10, choices=[('700mL', '700mL'), ('1000mL', '1000mL'), ('2000mL', '2000mL')])),
                ('loyalty_point', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Loyalty Codes 2',
            },
        ),
    ]
