from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import tiendaInfo, productoInfo
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'tiendas.html')
def productos(request):
    return render(request,'productos.html',{
        'lista_productos':productoInfo.objects.all()
    })
def tiendas(request):
    return render(request,'tiendas.html',{
        'lista_tiendas':tiendaInfo.objects.all()
    })
def detTiendas(request):
    return HttpResponse('Detalle de Tiendas')

def ingresoTiendas(request):
    print(request.POST)
    if request.method =='POST':
        nombreTie = request.POST.get('nombre')
        direccionTie = request.POST.get('direccion')
        provinciaTie = request.POST.get('provincia')
        regionTie = request.POST.get('region')
        fechaCreacionTie = request.POST.get('fechaCreacion')
        telefonoContactoTie = request.POST.get('telefonoContacto')
        tiendaInfo.objects.create(
            nombreTienda = nombreTie,
            direccionTienda = direccionTie,
            provinciaTienda = provinciaTie,
            regionTienda = regionTie,
            fechaCreacionTienda = fechaCreacionTie,
            telefonoContactoTienda = telefonoContactoTie
        )
        return HttpResponseRedirect(reverse('gestionTienda:tiendas'))
    return HttpResponse("Se recibio correctamente")
def eliminarTienda(request,tienda_id):
    objAlmacen = tiendaInfo.objects.get(id=tienda_id)
    objAlmacen.delete()
    return HttpResponseRedirect(reverse('gestionTienda:tiendas'))


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
        return HttpResponseRedirect(reverse('gestionTienda:productos'))
    return HttpResponse("Se recibio correctamente")
