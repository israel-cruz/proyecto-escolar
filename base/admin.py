from django.contrib import admin

from .models import Material, ListaMaterial, Clasificacion


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion','clasificacion')
    list_filter = ('clasificacion',)

class ListaMaterialAdmin(admin.ModelAdmin):
    model = ListaMaterial

    def id_material(self, obj):
        return obj.codigo.id

    def nombre_material(self, obj):
        return obj.codigo.nombre

    list_display = ['id','id_material','nombre_material','descripcion','cantidad', 'baja', 'fecha_actualizacion']
    list_editable = ['descripcion','cantidad']
    list_filter = ('fecha_actualizacion',)

admin.site.register(Material, MaterialAdmin)
admin.site.register(ListaMaterial, ListaMaterialAdmin)
admin.site.register(Clasificacion)
