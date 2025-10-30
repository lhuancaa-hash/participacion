from django.shortcuts import render, HttpResponse
from .forms import EquipoForm

def registro_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            nomEquipo = form.cleaned_data['nomEquipo']
            nombreJefe = form.cleaned_data['nombreJefe']
            membresia = form.cleaned_data['membresia']
            cantidad = form.cleaned_data['cantidad']
            total = membresia * cantidad

            datos = {
                'nomEquipo': nomEquipo,
                'nombreJefe': nombreJefe,
                'total': total
            }
            return render(request, 'Participacion/datosrecibidos.html', {'datos': datos})
    else:
        form = EquipoForm()

    return render(request, 'Participacion/formulario.html', {'form': form})
