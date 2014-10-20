#coding:utf-8
from django.db import models

# Create your models here.

FILME_OPCOES = [
      
      ('A','ACAO'),
      ('B','ADULTO'),
      ('C','ANIMACAO/DESENHOS'),
      ('D','AVENTURA'),
      ('E','COMEDIA'),
      ('F','DOCUMENTARIO'),
      ('G','DRAMA'),
      ('H','FICCAO_CIENTIFICA'),
      ('I','MUSICAL'),
      ('J','SUPENSE'),
      ('K','TERROR'),
      ('L','OUTROS')

]


class Filme(models.Model):
	
	NomeFilme = models.CharField('Nome',max_length=100)
	TipoFilme = models.CharField('Tipo de Filme',max_length=1,choices=TIPO_FILME,null=True)
	Codigo = models.CharField('Código do Filme',max_length=10,null=True)
	DataLancamento = models.DateField('Data de Lançamento',null=True)
	Prateleira = models.CharField('Numero da Prateleira',max_length=3)
	Setor = models.CharField('Nome do Setor',max_length=15)
	Produtora = models.EmailField('Nome da Empresa Produtora',max_length=100)
	 	
 	def __unicode__(self):
		return self.Filme
	
