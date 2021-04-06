from django.forms import *
from core.erp.models import Clientes

class ClientesForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

        self.fields['nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model = Clientes
        fields = '__all__'

        widgets = {
            'nro_documento': NumberInput(),
            'nro_telefono': NumberInput(),
            'direccion': TextInput(
                attrs={
                    'placeholder': 'Ejm: Av. La Campana',
                }
            ),
        }
        exclude = ['user_creation','user_updated']
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
            