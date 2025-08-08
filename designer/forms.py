
from django import forms
from .models import ShoeCustomization, ShoeModel

class CustomizationForm(forms.ModelForm):
    shoe = forms.ModelChoiceField(queryset=ShoeModel.objects.all(), label="Modelo de zapatilla")

    class Meta:
        model = ShoeCustomization
        fields = ['shoe', 'color', 'lace_color', 'sole_size', 'shape']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
            'lace_color': forms.TextInput(attrs={'type': 'color'}),
            'sole_size': forms.Select(choices=[('small','Pequeña'), ('medium','Mediana'), ('large','Grande')]),
            'shape': forms.TextInput(),
        }
