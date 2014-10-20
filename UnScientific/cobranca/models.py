#coding:utf-8
from django.db import models

# Create your models here.


CATEGORIA_FILME = [
      
      ('L','Lançamento'),
      ('P','Promocional'),
      ('N','Normal')

]

class Lancamento (models.Model):
	CategoriaFilme = models.CharField('Lançamento',max_length='L',choices=CATEGORIA_FILME)
	Valor = models.IntegerField('R$',max_length=5,null=True)
class Promocional (models.Model):
	CategoriaFilme = models.CharField('Promocional',max_length='P',choices=CATEGORIA_FILME)
	Valor = models.IntegerField('R$',max_length=5,null=True)
class Lancamento (models.Model):
	CategoriaFilme = models.CharField('Normal',max_length='N',choices=CATEGORIA_FILME)
	Valor = models.IntegerField('R$',max_length=5,null=True)

	
	def __unicode__(self):
		return self.CobrancaFilme



