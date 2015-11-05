# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_loyaltycodes2_loyalty_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('schedule', models.TextField()),
                ('address', models.CharField(max_length=500)),
                ('map_long', models.DecimalField(default=0.0, max_digits=11, decimal_places=8)),
                ('map_lat', models.DecimalField(default=0.0, max_digits=11, decimal_places=8)),
                ('is_featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.AddField(
            model_name='loyaltycodes2',
            name='tag_account',
            field=models.ForeignKey(to='main.Account', null=True),
        ),
    ]
