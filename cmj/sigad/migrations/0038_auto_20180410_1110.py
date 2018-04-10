# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-10 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sigad', '0037_remove_caixapublicacao_documentos'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaixaPublicacaoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem', models.PositiveIntegerField(default=0)),
                ('caixapublicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigad.CaixaPublicacao')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sigad.Documento')),
            ],
        ),
        migrations.AddField(
            model_name='caixapublicacao',
            name='documentos',
            field=models.ManyToManyField(blank=True, related_query_name='caixapublicacao_set', through='sigad.CaixaPublicacaoDocumento', to='sigad.Documento', verbose_name='Documentos da Caixa de Públicação'),
        ),
        migrations.AlterUniqueTogether(
            name='caixapublicacaodocumento',
            unique_together=set([('caixapublicacao', 'documento')]),
        ),
    ]