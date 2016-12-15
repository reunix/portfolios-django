from django.contrib import admin
from models import DadosPessoais
# Register your models here.


class DadosPessoaisAdmin(admin.ModelAdmin):
    save_on_top=True
    list_display = ['name','mobile','email']
    list_filter = ['sexo']
    search_fields = ['name']


admin.site.register(DadosPessoais, DadosPessoaisAdmin)



# admin.site.register(DadosPessoais)


