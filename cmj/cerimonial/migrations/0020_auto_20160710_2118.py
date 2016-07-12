# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0019_processo_workspace'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processo',
            old_name='responsavel',
            new_name='responsaveis',
        ),
        migrations.AlterField(
            model_name='processo',
            name='data',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Abertura'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='observacoes',
            field=models.TextField(blank=True, default='', verbose_name='Outras observações sobre o Processo'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='processo_set', to='cerimonial.StatusProcesso', verbose_name='Status do Processo'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='titulo',
            field=models.CharField(max_length=254, verbose_name='Título'),
        ),
    ]