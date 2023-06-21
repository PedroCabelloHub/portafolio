from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import JugadorForm, DirectorForm, EquiposForm, LigasForm, EstadiosForm, ArbitrosForm, JuegosForm
from .models import Jugadores, Directores, Equipos, Ligas, Estadios, Arbitros, Juegos

def index(request):
    title = "Manager Teams"
    return render(request,'index.html')

from .forms import JugadorForm

def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir o realizar alguna acción adicional
    else:
        form = JugadorForm()
    return render(request, 'crear_jugador.html', {'form': form})

def crear_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir o realizar alguna acción adicional
    else:
        form = DirectorForm()
    return render(request, 'crear_director.html', {'form': form})


def crear_equipo(request):
    if request.method == 'POST':
        form = EquiposForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir o realizar alguna acción adicional
    else:
        form = EquiposForm()
    return render(request, 'crear_equipo.html', {'form': form})


def crear_liga(request):
    if request.method == 'POST':
        form = LigasForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir o realizar alguna acción adicional
    else:
        form = LigasForm()
    return render(request, 'crear_liga.html', {'form': form})


def crear_estadio(request):
    if request.method == 'POST':
        form = EstadiosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir o realizar alguna acción adicional
    else:
        form = EstadiosForm()
    return render(request, 'crear_estadio.html', {'form': form})


def crear_arbitro(request):
    if request.method == 'POST':
        form = ArbitrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir o realizar alguna acción adicional
    else:
        form = ArbitrosForm()
    return render(request, 'crear_arbitro.html', {'form': form})


def crear_juego(request):
    if request.method == 'POST':
        form = JuegosForm(request.POST, request.FILES)
        if form.is_valid():
            juego = form.save(commit=False)  # Obtener instancia del juego sin guardar en la base de datos
            equipo1 = juego.equipo1
            equipo2 = juego.equipo2

            if equipo1.ligas.id != equipo2.ligas.id:
                form.add_error(None, "Los equipos no pertenecen a la misma liga.")
            else:
                juego.save()  # Guardar el juego en la base de datos si pasa la validación

    else:
        form = JuegosForm()
    return render(request, 'crear_juego.html', {'form': form})


def equipo_detail(request,id):
    equipo = get_object_or_404(Equipos, id=id)
    jugadores = Jugadores.objects.filter(equipo_id=id)
    return render(request, 'equipo_detail.html', {
        'equipo': equipo,
        'jugadores':jugadores
    })

def liga_detail(request,id):
    liga = get_object_or_404(Ligas, id=id)
    equipos = Equipos.objects.filter(ligas_id=id)
    return render(request, 'liga_detail.html', {
        'liga': liga,
        'equipos': equipos
    })


def lista_equipos(request):
    equipos = Equipos.objects.all()
    return render(request, 'equipos_list.html', {'equipos': equipos})

def lista_liga(request):
    ligas = Ligas.objects.all()
    return render(request, 'liga_list.html', {'ligas': ligas})


def lista_estadios(request):
    estadios = Estadios.objects.all()
    return render(request, 'estadios_list.html', {'estadios': estadios})


def lista_arbitros(request):
    arbitros = Arbitros.objects.all()
    return render(request, 'arbitros_list.html', {'arbitros': arbitros})

def lista_jugadores(request):
    jugadores = Jugadores.objects.all()
    return render(request, 'jugadores_list.html', {'jugadores': jugadores})


def lista_directores(request):
    directores = Directores.objects.all()
    return render(request, 'directores_list.html', {'directores': directores})

def lista_juegos(request):
    juegos = Juegos.objects.all()
    return render(request, 'juegos_list.html', {'juegos': juegos})
