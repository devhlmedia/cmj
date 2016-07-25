# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20160722_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bairro',
            name='codigo',
            field=models.PositiveIntegerField(blank=True, help_text='Código do Bairro no Cadastro Oficial do Município', verbose_name='Código'),
        ),
    ]