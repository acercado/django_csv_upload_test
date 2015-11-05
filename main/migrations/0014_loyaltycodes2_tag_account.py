# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_loyaltycodes2_tag_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='loyaltycodes2',
            name='tag_account',
            field=models.ForeignKey(to='main.Account', blank=True, null=True),
        ),
    ]
