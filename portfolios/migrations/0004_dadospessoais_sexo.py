# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0003_dadospessoais_contato'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadospessoais',
            name='sexo',
            field=models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], default='masculino', max_length=50),
            preserve_default=False,
        ),
    ]
