# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0002_auto_20160622_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localtrabalho',
            name='cep',
            field=models.CharField(blank=True, default='', max_length=9, verbose_name='CEP'),
        ),
    ]