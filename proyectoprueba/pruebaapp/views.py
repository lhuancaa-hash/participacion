from django.shortcuts import render, HttpResponse
from datetime import datetime
from .forms import ClienteForm 

# Create your views here.
def saludo(request):
    #desplazar contenido sobre el nav
    return HttpResponse("Hola les saluda Django")


def info_usuario(request):
    nombre = "Alan Brito"
    edad = 25
    return HttpResponse(f"Hola soy {nombre} mi edad {edad}")

def saludo_mejorado(reques, nombre, edad):
    return HttpResponse(f"Hola soy {nombre} mi edad {edad}")

def tabla_multiplicar(request, numero):
    num = numero
    resultado = ""
    for i in range (1,11):
        resultado = resultado + f"{num} * {i} = {num * i} <br>"
    return HttpResponse(resultado)

def saludo2(request):
    datos ={
        'nombre': 'Alan Brito',
        'edad': 25
    }
    return render(request, 'saludo.html', datos)

def info(request):
    return render(request, 'informacion.html')


def nuevo_saludo(request, nombre, edad):
    return render(request, 'nuevoSaludo.html',{'nom' : nombre , 'edad' : edad})

def tabla_producto(request, num):
    lista = []
    for i in range(1,11):
        lista.append({'i' : i,'res' : i*num})
    return render(request, 'tabla_multiplicar.html', {'lista' : lista, 'num' : num})


#aca definimos la vista
#solicitud = request
def formulario_cliente(request):
    datos = None
    if request.method == 'POST':
        #aca se recuperan los datos del form
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        anioNac = request.POST.get('anioNac')
        pais = request.POST.get('pais')

        edad = datetime.now().year - int(anioNac)

        datos = {
            'nombre':nombre,
            'correo':correo,
            'anioNac':anioNac,
            'edad':edad,
            'pais':pais
        } 

    #ingreso por un url o enlace
    return render(request, 'formulario.html', {'datos':datos})

def crear_cliente(request):
    datos = None
    if request.method == 'POST':
        form = ClienteForm(request.POST)#crenado un obj de la clase clienteform
        if form.is_valid():  # ✅ Verifica primero si el formulario es válido
            datos = form.cleaned_data  # ✅ Ahora sí puedes acceder a cleaned_data
            return render(request, 'cliente_exito.html', {'datos':datos})
    else:
        inicial={
            'nombre':'',
            'correo':'',
            'anioNac':'',
            'pais':''
        }
        form = ClienteForm(initial=inicial)
        return render(request,'cliente_form.html',{'form':form})

