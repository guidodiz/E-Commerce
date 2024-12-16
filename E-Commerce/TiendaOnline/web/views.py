from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils.timezone import now
from django.core.mail import send_mail
from django.conf import settings
from .models import Productos, Compras, Cliente
from .forms import CompraModelForm

def index(request):
    time = now()
    productos = Productos.objects.filter(tiene_descuento=True)

    context = {
        'time': time,
        'productos': productos
    }

    return render(request, 'web/index.html', context)

def productos(request):
    time = now()
    productos = Productos.objects.all()

    context = {
        'time': time,
        'productos': productos
    }
    
    return render(request, 'web/productos.html', context)

def novedades(request):
    time = now()

    context = {
        'time': time,
    }

    return render(request, 'web/novedades.html', context)

def vista_producto(request, id):
    time = now()
    producto = Productos.objects.get(id=id)
    
    context = {
        'time': time,
        'producto': producto
    }

    return render(request, 'web/vista_producto.html', context)

def compra(request):
    context = {}

    producto_id = request.GET.get('producto_id')
    talle = request.GET.get('talle')
    cantidad = int(request.GET.get('cantidad', 1))
    producto = None
    form = None

    if producto_id:
        producto = Productos.objects.get(id=producto_id)
        precio = producto.precio_nuevo if producto.precio_nuevo else producto.precio_original 

        if not talle:
            talle = producto.talle1

        initial_data = {
            'producto': producto.nombre,
            'talle': talle,
            'cantidad': cantidad,
            'precio': precio,
        }

        form = CompraModelForm(initial=initial_data)

    if request.method == "POST":
        form = CompraModelForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            cliente = Cliente.objects.create(
                nombre=request.POST['nombre'],
                email=request.POST['email'],
                telefono=request.POST['telefono']
            )

            compra.cliente = cliente
            compra.save()

#----------------------------------------------------------------------------

            asunto_cliente = "Detalles de la compra"
            mensaje_cliente = f"""
            Hola {cliente.nombre}, ¡gracias por tu compra!
            
            Detalles de la compra:
            {compra.producto}
            Talle: {compra.talle}
            Cantidad: {compra.cantidad}
            Precio: {compra.precio}
            Medio de Pago: {compra.medio_de_pago}
            {compra.envio}

            """
            if compra.medio_de_pago == "Transferencia":
                mensaje_cliente += """
            Información para transferir:
            - Banco: XYZ
            - CBU: 00000000000000000000
            - Alias: ARCANAIN.DUMENTARIA
            - Titular: Arcana Indumentaria
            """
            elif compra.medio_de_pago == "MP":
                mensaje_cliente += """
            Información para transferir:
            - Cuenta: Mercado Pago
            - Alias: guidodiz.mp
            - CVU: 0000003100002830997264
            """

            send_mail(asunto_cliente, mensaje_cliente, settings.DEFAULT_FROM_EMAIL, [cliente.email])


            asunto_admin = "Nueva Compra Realizada"
            mensaje_admin = f"""
            Se ha realizado una nueva compra.

            Datos del cliente:
            Nombre: {cliente.nombre}
            Email: {cliente.email}
            Teléfono: {cliente.telefono}

            Detalles de la compra:
            {compra.producto}
            Talle: {compra.talle}
            Cantidad: {compra.cantidad}
            Precio: {compra.precio}
            Medio de Pago: {compra.medio_de_pago}
            {compra.envio}
            """

            send_mail(asunto_admin, mensaje_admin, settings.DEFAULT_FROM_EMAIL, ["guidoangeldiz@gmail.com"])

            messages.success(request, '¡Gracias por realizar tu compra!')
            return redirect('index')
        else:
            messages.error(request, 'Ocurrió un error. Revisa los datos e intenta de nuevo.')

    context['form'] = form
    return render(request, 'web/compra.html', context)