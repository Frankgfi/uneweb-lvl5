from .models import Persona
from django import forms

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['DNI', 'nombres', 'apellidos', 'sexo', 'fecha_nacimiento', 'direccion', 'telefono', 'correo']
        widgets = {
            'fecha_nacimiento':forms.DateInput(attrs={'type':'date'})
        }
        
