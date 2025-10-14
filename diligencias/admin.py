from django.contrib import admin

from diligencias.models import Diligencia

class DiligenciaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'data_realizacao', 'dinheiro_apreendido']
    search_fields = ['nome', 'data_realizacao']
    list_filter = ['data_realizacao']

admin.site.register(Diligencia, DiligenciaAdmin)
