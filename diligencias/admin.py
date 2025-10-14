from django.contrib import admin
from diligencias.models import Diligencia

@admin.register(Diligencia)
class DiligenciaAdmin(admin.ModelAdmin):
    # Troque 'data_realizacao' por 'data_formatada' na listagem
    list_display = ['nome', 'data_formatada', 'dinheiro_apreendido']
    search_fields = ['nome', 'data_realizacao']
    list_filter = ['data_realizacao']

    @admin.display(description='Data Realização')
    def data_formatada(self, obj):
        # dd/mm/aaaa
        return obj.data_realizacao.strftime('%d/%m/%Y')
