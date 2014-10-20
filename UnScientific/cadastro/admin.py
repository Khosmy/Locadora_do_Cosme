#coding:utf-8
from django.contrib import admin
from models import Pessoa

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
	list_display = ['Nome','CPF']
	list_filter = ['Sexo']
	search_fields = ['Nome','CPF']
	
admin.site.register(Pessoa,PessoaAdmin)
