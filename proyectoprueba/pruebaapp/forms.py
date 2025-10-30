from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="nombre", required=True)
    correo = forms.EmailField(label="correo",required=True)
    anioNac = forms.IntegerField(label="anioNac", required=True)
    pais = forms.CharField(label="pais", required=True)