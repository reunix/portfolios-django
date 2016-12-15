# coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DadosPessoais(models.Model):


    SEXO_CHOICES = (
        (u'masculino', u'Masculino'),
        (u'feminino', u'Feminino')
    )


    name = models.CharField(max_length=50, verbose_name='Nome')
    adress = models.CharField(max_length=100, verbose_name='Endereço')
    city = models.CharField(max_length=50, verbose_name='Cidade')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    cep = models.CharField(max_length=50, verbose_name='Cep')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    mobile = models.CharField(max_length=20, verbose_name='Celular')

    sexo = models.CharField(max_length=50, choices = SEXO_CHOICES)

    contato = models.CharField(max_length=20, verbose_name='Contato')

    about = models.TextField(max_length=255, verbose_name='Sobre')
    data_nascimento = models.CharField(max_length=255, default='01 de janeiro de 2000', verbose_name='Data Nascimento')
    email = models.EmailField(verbose_name='Email')


    conhecimentos = models.TextField(max_length=255, verbose_name='Conhecimentos')
    github = models.CharField(max_length=100, default='http://github.com/SeuGit', verbose_name='Github')
    current_position = models.CharField(max_length=100, verbose_name='Cargo atual')
    empresa = models.CharField(max_length=100, verbose_name='Empresa')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dados Pessoais'
        verbose_name_plural = 'Dados Pessoais'