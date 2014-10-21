#coding:utf-8
from django.contrib import admin
from models import Pessoa

# Register your models here.

class CadastraFilme(admin.ModelCadastra):
	list_display = ['NomeFilme','TipoFilme','DataLancamento','Produtora']
	list_filter = ['Codigo','Prateleira','Setor']
	search_fields = ['NomeFilme','Produtora']
	
admin.site.register(Filme,CadastraFilme)
