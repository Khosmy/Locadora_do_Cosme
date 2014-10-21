#coding:utf-8
from django.contrib import admin
from models import Pessoa

# Register your models here.

class CadastraFilme(admin.ModelCadastra):
	list_display = ['NomeFilme','TipoFilme','DataLancamento','Produtora','Codigo','Prateleira','Setor']
	list_filter = ['NomeFilme']
	search_fields = ['NomeFilme','Produtora']
	
admin.site.register(Filme,CadastraFilme)
