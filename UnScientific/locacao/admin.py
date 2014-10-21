#coding:utf-8
from django.contrib import admin
from models import Filme


class locacaoFilme(admin.ModelLocacao):
	list_display = ['NomeLocador','NomeFilme','DataAluguel','TipoFilme','CategoriaFilme','DataDevolucao']
	list_filter = ['NomeFilme','NomeLocador']
	search_fields = ['TipoFilme','CategoriaFilme']
	save_as = True
	
admin.site.register(Filme,LocacaoFilme)	









# Register your models here.
