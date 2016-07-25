# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20160722_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bairro',
            name='codigo',
            field=models.PositiveIntegerField(default=0, help_text='Código do Bairro no Cadastro Oficial do Município', verbose_name='Código'),
        ),
    ]