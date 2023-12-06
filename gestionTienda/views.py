from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import tiendaInfo, productoInfo

# Create your views here.
def index(request):
    return HttpResponse('Bienvenidos')
def productos(request):
    return HttpResponse('Productos')
def tiendas(request):
    return HttpResponse('Tiendas')
def detTiendas(request):
    return HttpResponse('Detalle de Tiendas')

def ingresoTiendas(request):
    print(request.POST)
    if request.method =='POST':
        direccionTie = request.POST.get('direccion')
        provinciaTie = request.POST.get('provincia')
        regionTie = request.POST.get('region')
        fechaCreacionTie = request.POST.get('fechaCreacion')
        telefonoContactoTie = request.POST.get('telefonoContacto')
        tiendaInfo.objects.create(
            direccionTienda = direccionTie,
            provinciaTienda = provinciaTie,
            regionTienda = regionTie,
            fechaCreacionTienda = fechaCreacionTie,
            telefonoContactoTienda = telefonoContactoTie
        )
        return HttpResponseRedirect(reverse('app2:inicio'))
    return HttpResponse("Se recibio correctamente")

def ingresoProductos(request):
    print(request.POST)
    if request.method =='POST':
        descripcionPro = request.POST.get('descripcion')
        codigoPro = request.POST.get('codigo')
        precioVentaPro = request.POST.get('precioVenta')
        cantidadPro = request.POST.get('cantidad')
        productoInfo.objects.create(
            descripcionProducto = descripcionPro,
            codigoProducto = codigoPro,
            pvProducto = precioVentaPro,
            cantidadProducto = cantidadPro,
        )
        return HttpResponseRedirect(reverse('app2:inicio'))
    return HttpResponse("Se recibio correctamente")
