from django.contrib import admin
from cof.models import Machine,Pod


class MachineAdmin(admin.ModelAdmin):
    list_filter = ('product_type','water_line_compitable','model')
admin.site.register(Machine,MachineAdmin)

class PodAdmin(admin.ModelAdmin):
    list_filter = ('product_type','flavor','pack_size')
admin.site.register(Pod,PodAdmin)
