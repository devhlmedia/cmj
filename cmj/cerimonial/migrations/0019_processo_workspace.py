# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160710_2004'),
        ('cerimonial', '0018_auto_20160710_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo',
            name='workspace',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='processo_set', to='core.AreaTrabalho', verbose_name='Área de Trabalho'),
            preserve_default=False,
        ),
    ]