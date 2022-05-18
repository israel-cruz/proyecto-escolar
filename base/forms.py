from django.forms import ModelForm

from .models import Material, ListaMaterial

class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        exclude = ['usuario']

class EntradaMaterialForm(ModelForm):
    class Meta:
        model = ListaMaterial
        fields = '__all__'
        exclude = ['usuario','fecha_actualizacion']
