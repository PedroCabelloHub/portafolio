from django import forms
from .models import Jugadores, Directores, Equipos, Ligas, Estadios, Arbitros, Juegos

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugadores
        fields = ('name', 'posicion', 'num_player','equipo_id' ,'foto')

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Directores
        fields = ('name', 'foto')

class EquiposForm(forms.ModelForm):
    class Meta:
        model = Equipos
        fields = ('name', 'foto', 'directores','ligas')


class LigasForm(forms.ModelForm):
    class Meta:
        model = Ligas
        fields = ('name', 'foto')

class EstadiosForm(forms.ModelForm):
    class Meta:
        model = Estadios
        fields = ('name','liga_id' ,'foto')

        

class ArbitrosForm(forms.ModelForm):
    class Meta:
        model = Arbitros
        fields = ('name' ,'foto','liga_id')

        

class JuegosForm(forms.ModelForm):

    fecha = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
    )

    class Meta:
        model = Juegos
        fields = ('folio' ,'fecha','liga_id', 'equipo1', 'equipo2', 'estadio', 'arbitro', 'state')