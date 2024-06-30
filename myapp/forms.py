## Cadastra Cliente          
from django import forms

from myapp.models import Inspetor, RegistraVistoria, Vistoria

## Cadastra a vistoria
class InspetorForm(forms.ModelForm):
    class Meta:
        model = Inspetor
        fields = '__all__'
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'


class MultipleFileInput(forms.ClearableFileInput):
  allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

## Cadastra um Visotria
class VistoriaForm(forms.ModelForm):
    vistoria = MultipleFileField()
    class Meta:
        model = Vistoria
        fields = '__all__'
        exclude = ('esta_vistoriado',)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            if field.widget.__class__ in [forms.CheckboxInput, forms.RadioSelect]:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


## Registra Vistoria    
class RegistraVistoriaForm(forms.ModelForm):
    dt_inicio = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date',}))
    dt_fim = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date',}))

    class Meta:
        model = RegistraVistoria
        fields = '__all__'
        exclude = ('vistoria','create_at',)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'