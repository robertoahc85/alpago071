from django import forms
from .models import School

class SchoolAdminForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añadir placeholders a los campos específicos
        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Ejemplo: 5551234567',
            'maxlength': '15',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'correo@ejemplo.com',
        })
        self.fields['website'].widget.attrs.update({
            'placeholder': 'https://www.ejemplo.com',
        })
