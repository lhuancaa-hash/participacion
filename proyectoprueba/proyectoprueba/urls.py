"""
URL configuration for proyectoprueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from pruebaapp import views
from Participacion import views

#A MANERA DE LIBRERIA
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('saludo/', views.saludo),
    #path('saludo_usuario/',views.info_usuario),
    #path('saludov2/<str:nombre>/<int:edad>/',views.saludo_mejorado),
    #path('tabla/<int:numero>',views.tabla_multiplicar),
    #path('saludo2/', views.saludo2, name='saludo2'),
    #path('informacion/', views.info, name='informacion'),
    #path('nuevo_saludo/<str:nombre>/<int:edad>/',views.nuevo_saludo, name='nuevo_saludo'),
    #path('tabla_multi/<int:num>/',views.tabla_producto,name='tabla_product'),
    #path('formulario/',views.formulario_cliente, name='formulario_cliente'),
    #path('nuevo/',views.crear_cliente,name='crear_cliente'),
    path('formulario_equipo/', views.registro_equipo, name='registrar_equipo')
]
