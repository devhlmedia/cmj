# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160710_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImpressoEnderecamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome do Impresso')),
                ('tipo', models.CharField(choices=[('ET', 'Folha de Etiquetas'), ('EV', 'Envelopes')], default='ET', max_length=2, verbose_name='Tipo do Impresso')),
                ('largura_pagina', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Largura da Página')),
                ('altura_pagina', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Altura da Página')),
                ('margem_esquerda', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Margem Esquerda')),
                ('margem_superior', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Margem Superior')),
                ('colunasfolha', models.PositiveSmallIntegerField(verbose_name='Colunas')),
                ('linhasfolha', models.PositiveSmallIntegerField(verbose_name='Linhas')),
                ('larguraetiqueta', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Largura da Etiqueta')),
                ('alturaetiqueta', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Altura da Etiquta')),
                ('entre_colunas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('entre_linhas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fontesizebase', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name_plural': 'Impressos para Endereçamento',
                'verbose_name': 'Impresso para Endereçamento',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('menu_dados_auxiliares', 'Mostrar Menu Dados Auxiliares'), ('menu_tabelas_auxiliares', 'Mostrar Menu de Tabelas Auxiliares'), ('menu_contatos', 'Mostrar Menu de Cadastro de Contatos'), ('menu_processos', 'Mostrar Menu de Cadastro de Processos'), ('menu_area_trabalho', 'Mostrar Menu de Áreas de Trabalho'), ('menu_impresso_enderecamento', 'Mostrar Menu de Impressos de Endereçamento'))},
        ),
    ]