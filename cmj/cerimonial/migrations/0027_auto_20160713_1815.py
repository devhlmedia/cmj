# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 21:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0026_auto_20160712_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assuntoprocesso',
            options={'ordering': ('descricao',), 'verbose_name': 'Assunto de Processo', 'verbose_name_plural': 'Assuntos de Processos'},
        ),
        migrations.AlterModelOptions(
            name='classificacaoprocesso',
            options={'ordering': ('descricao',), 'verbose_name': 'Classificacao de Processo', 'verbose_name_plural': 'Classificações de Processos'},
        ),
        migrations.AlterModelOptions(
            name='estadocivil',
            options={'ordering': ('descricao',), 'verbose_name': 'Estado Civil', 'verbose_name_plural': 'Estados Civis'},
        ),
        migrations.AlterModelOptions(
            name='nivelinstrucao',
            options={'ordering': ('descricao',), 'verbose_name': 'Nível de Instrução', 'verbose_name_plural': 'Níveis de Instrução'},
        ),
        migrations.AlterModelOptions(
            name='operadoratelefonia',
            options={'ordering': ('descricao',), 'verbose_name': 'Operadora de Telefonia', 'verbose_name_plural': 'Operadoras de Telefonia'},
        ),
        migrations.AlterModelOptions(
            name='parentesco',
            options={'ordering': ('descricao',), 'verbose_name': 'Parentesco', 'verbose_name_plural': 'Parentescos'},
        ),
        migrations.AlterModelOptions(
            name='processo',
            options={'ordering': ('titulo',), 'verbose_name': 'Processo', 'verbose_name_plural': 'Processos'},
        ),
        migrations.AlterModelOptions(
            name='statusprocesso',
            options={'ordering': ('descricao',), 'verbose_name': 'Status de Processo', 'verbose_name_plural': 'Status de Processos'},
        ),
        migrations.AlterModelOptions(
            name='tipoautoridade',
            options={'ordering': ('descricao',), 'verbose_name': 'Tipo de Autoridade', 'verbose_name_plural': 'Tipos de Autoridade'},
        ),
        migrations.AlterModelOptions(
            name='tipoemail',
            options={'ordering': ('descricao',), 'verbose_name': 'Tipo de Email', 'verbose_name_plural': 'Tipos de Email'},
        ),
        migrations.AlterModelOptions(
            name='tipoendereco',
            options={'ordering': ('descricao',), 'verbose_name': 'Tipo de Endereço', 'verbose_name_plural': 'Tipos de Endereço'},
        ),
        migrations.AlterModelOptions(
            name='tipolocaltrabalho',
            options={'ordering': ('descricao',), 'verbose_name': 'Tipo do Local de Trabalho', 'verbose_name_plural': 'Tipos de Local de Trabalho'},
        ),
        migrations.AlterModelOptions(
            name='tipotelefone',
            options={'ordering': ('descricao',), 'verbose_name': 'Tipo de Telefone', 'verbose_name_plural': 'Tipos de Telefone'},
        ),
        migrations.AlterModelOptions(
            name='topicoprocesso',
            options={'ordering': ('descricao',), 'verbose_name': 'Tópico de Processo', 'verbose_name_plural': 'Tópicos de Processos'},
        ),
    ]
