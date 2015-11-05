# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_loyaltycodes2_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='loyaltycodes2',
            name='volume',
            field=models.CharField(choices=[('700mL', '700mL'), ('1000mL', '1000mL'), ('2000mL', '2000mL')], max_length=10, default='700mL'),
        ),
    ]
