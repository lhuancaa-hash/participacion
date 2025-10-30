from django import forms

class EquipoForm(forms.Form):
    nomEquipo = forms.CharField(label="Nombre del equipo", max_length=100)
    
    # Combo con nombres
    OPCIONES_NOMBRES = [
        ('Aguilar Machicado Nils Reiner', 'Aguilar Machicado Nils Reiner'),
        ('Aguirre Chuquimia Ana Camila', 'Aguirre Chuquimia Ana Camila'),
        ('Balboa Machicado Jhonathan Raul', 'Balboa Machicado Jhonathan Raul'),
        ('Huanca Ancalle Lenny Daline', 'Huanca Ancalle Lenny Daline'),
        ('Serrano Mamani Raquel Araceli', 'Serrano Mamani Raquel Araceli'),
    ]
    nombreJefe = forms.ChoiceField(choices=OPCIONES_NOMBRES, label="Nombre del jefe")
    
    membresia = forms.IntegerField(label="Membresía")
    cantidad = forms.IntegerField(label="Cantidad", initial=0)
