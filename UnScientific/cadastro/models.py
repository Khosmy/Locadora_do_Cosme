#coding:utf-8
from django.db import models

# Create your models here.

SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino')

]

ESTADO_OPCOES = [
	('AC','Acre - AC'),
	('AL','Alagoas - AL'),
	('AP','Amapá - AP'),
	('AM','Amazonas - AM'),
	('BA','Bahia  - BA'),
	('CE','Ceará - CE'),
	('DF','Distrito Federal  - DF'),
	('ES','Espírito Santo - ES'),
	('GO','Goiás - GO'),
	('MA','Maranhão - MA'),
	('MT','Mato Grosso - MT'),
	('MS','Mato Grosso do Sul - MS'),
	('MG','Minas Gerais - MG'),
	('PA','Pará - PA'),
	('PB','Paraíba - PB'),
	('PR','Paraná - PR'),
	('PE','Pernambuco - PE'),
	('PI','Piauí - PI'),
	('RJ','Rio de Janeiro - RJ'),
	('RN','Rio Grande do Norte - RN'),
	('RS','Rio Grande do Sul - RS'),
	('RO','Rondônia - RO'),
	('RR','Roraima - RR'),
	('SC','Santa Catarina - SC'),
	('SP','São Paulo - SP'),
	('SE','Sergipe - SE'),
	('TO','Tocantins - TO')
]

class Pessoa(models.Model):
	
	Nome = models.CharField('Nome',max_length=100)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES)
	CPF = models.CharField('CPF',max_length=15)
	DataNascimento = models.DateField('Data de Nascimento')
	Telefone = models.CharField('Telefone',max_length=15)
	Celular = models.CharField('Celular',max_length=15)
	Email = models.EmailField('Endereço de email',max_length=100)
	Logradouro = models.CharField('Logradouro', max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
 	UF = models.CharField('UF', max_length=2,choices=ESTADO_OPCOES)
 	CEP = models.CharField('CEP', max_length=9,null=True)	
 	URL = models.URLField ('Página Pessoal', max_length=200,null=True)
 	
 	def __unicode__(self):
		return self.Nome
	
