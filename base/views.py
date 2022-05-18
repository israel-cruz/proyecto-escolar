from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Material, ListaMaterial, Clasificacion
from .forms import MaterialForm, EntradaMaterialForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'El usuario o contraseña son incorrectos.')

    return render(request, 'base/login_register.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'base/home.html')

@login_required(login_url='login')
def lista_material(request):
    material = Material.objects.all()
    cantidad = material.count()

    context = {
        'lista':material,
        'cantidad':cantidad,
    }

    return render(request, 'base/listado_material.html', context)

@login_required(login_url='login')
def gestion_material(request):

    lista_material = ListaMaterial.objects.all()
    cantidad_registros = lista_material.count()

    context = {
        'lista':lista_material,
        'cantidad':cantidad_registros
    }
    return render(request, 'base/gestion_material.html', context)

@login_required(login_url='login')
def registrar_material(request):
    form = MaterialForm()
    clasificaciones = Clasificacion.objects.all()
    
    if request.method == 'POST':
        clasificacion = request.POST.get('clasificacion')
        clasif, created = Clasificacion.objects.get_or_create(nombre=clasificacion)

        Material.objects.create(
            usuario = request.user,
            nombre = request.POST.get('nombre'),
            descripcion = request.POST.get('descripcion'),
            clasificacion = clasif
        )
        return redirect('home')
    
    context = {
        'form':form,
        'clasificaciones':clasificaciones,
    }
    
    return render(request, 'base/registrar_material.html', context)

@login_required(login_url='login')
def modificar_material(request, pk):
    material = Material.objects.get(id=pk)
    form = MaterialForm(instance=material)
    clasificaciones = Clasificacion.objects.all()

    if request.user != material.usuario:
        return HttpResponse('No puedes modificar este material ya que no lo has registrado tu!')

    if request.method == 'POST':
        clasificacion = request.POST.get('clasificacion')
        clasif, created = Clasificacion.objects.get_or_create(nombre=clasificacion)
        material.nombre = request.POST.get('nombre')
        material.descripcion = request.POST.get('descripcion')
        material.clasificacion = clasif
        material.save()
        return redirect('home')
    
    context = {
        'form':form,
        'clasificaciones':clasificaciones,
        'material':material
    }

    return render(request, 'base/registrar_material.html', context)
    
@login_required(login_url='login')
def entrada_material(request):
    materiales = Material.objects.all()
    form = EntradaMaterialForm()
    
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        material = Material.objects.get(id=codigo)

        ListaMaterial.objects.create(
            usuario = request.user,
            codigo = material,
            descripcion = request.POST.get('descripcion'),
            cantidad = request.POST.get('cantidad'),
        )
        return redirect('home')
    
    context = {
        'form':form,
        'materiales':materiales,
    }

    return render(request, 'base/entrada_material.html', context)

@login_required(login_url='login')
def baja_material(request, pk):
    material = ListaMaterial.objects.get(id=pk)

    if request.method == 'POST':
        material.cantidad = 0
        material.baja = request.POST.get('baja')
        material.save()
        return redirect('home')
    
    context = {
        'material':material
    }

    return render(request, 'base/baja_material.html', context)