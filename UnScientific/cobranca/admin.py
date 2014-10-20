#coding:utf-8
from django.contrib import admin
from models import Locacao
from models import Filme


class CobrancaFilme(admin.ModelCobranca):
	list_display = ['Lancamento','Promocional','Lancamento']
	list_filter = ['NomeFilme']
	search_fields = ['Valor','CategoriaFilme']
	save_as = True
	
admin.site.register(Filme,CobrancaFilme)	









# Register your models here.
