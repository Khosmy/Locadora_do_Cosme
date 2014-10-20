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


class AluguelFilme (models.Model):
	NomeFilme = models.CharField('Nome do filme',max_length=100,null=True)
	TipoFilme = models.CharField('Tipo de Filme',max_length=1,choices=TIPO_FILME,null=True)
	CategoriaFilme = models.CharField('Categoria do Filme',max_length=1,choices=CATEGORIA_FILME,null=True)
	DataAluguel = models.DateTimeField('Data do Aluguel',null=True)
	NomeLocador = models.CharField('Nome do Locador',max_length=100,null=True)
	DataDevolucao = models.DateTimeField('Data do Aluguel',null=True)
	NumDiarias = models.IntegerField('Numero de dias alugado',null=True)
	
	def __unicode__(self):
		return self.AluguelFilme
