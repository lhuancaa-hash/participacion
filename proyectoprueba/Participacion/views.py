from django.shortcuts import render, HttpResponse
from .forms import EquipoForm

def registro_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            nombreEquipo = form.cleaned_data['nomEquipo']
            nombreJefe = form.cleaned_data['nombreJefe']
            membresia = form.cleaned_data['membresia']
            cantidad = form.cleaned_data['cantidad']
            total = membresia * cantidad

            datos = {
                'nombreEquipo': nombreEquipo,
                'nombreJefe': nombreJefe,
                'membresia': membresia,
                'cantidad': cantidad,
                'total': total
            }
            return render(request, 'datosrecibidos.html', {'datos': datos})
        else:
            # Si el formulario no es válido, se immprimir errores en consola
            print(form.errors)
    else:
        form = EquipoForm()

    return render(request, 'formulario.html', {'form': form})
