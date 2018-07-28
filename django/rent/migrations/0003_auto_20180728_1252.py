# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-28 12:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_rentalpayment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ('price',), 'verbose_name_plural': 'Properties'},
        ),
        migrations.AddField(
            model_name='property',
            name='rent_length',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(120)]),
            preserve_default=False,
        ),
    ]