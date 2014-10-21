#coding:utf-8
from django.db import models

# Create your models here.

TIPO_FILME = [
      
      ('A','ACAO'),
      ('B','ADULTO'),
      ('C','ANIMACAO/DESENHOS'),
      ('D','AVENTURA'),
      ('E','COMEDIA'),
      ('F','DOCUMENTARIO'),
      ('G','FICCAO_CIENTIFICA'),
      ('H','MUSICAL'),
      ('I','SUPENSE'),
      ('J','TERROR'),
      ('K','OUTROS')

]

CATEGORIA_FILME = [
      
      ('L','Lançamento'),
      ('P','Promocional'),
      ('N','Normal')

]

STATUS_LOCADOR = [
      
      ('I','Inadiplente'),
      ('A','Adiplente'),

]


class AluguelFilme (models.Model):
	NomeFilme = models.CharField('Nome do filme',max_length=100,null=True)
	TipoFilme = models.CharField('Tipo de Filme',max_length=1,choices=TIPO_FILME,null=True)
	CategoriaFilme = models.CharField('Categoria do Filme',max_length=1,choices=CATEGORIA_FILME,null=True)
	NomeLocador = models.CharField('Nome do Locador',max_length=100,null=True)
	StatusLocador = models.CharField('Condição do Locador',max_length=1,choices=STATUS_LOCADOR,null=True)

	
	def __unicode__(self):
		return self.AluguelFilme
