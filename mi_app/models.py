from django.db import models


class Directores(models.Model):
    name = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='directores/')

    def __str__(self):
        return self.name

class Ligas(models.Model):
    name = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='ligas/')
    
    def __str__(self):
        return self.name

class Equipos(models.Model):
    name = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='equipos/')
    directores = models.ForeignKey(Directores, on_delete=models.SET_NULL,null=True,related_name='equipos_directores')
    ligas = models.ForeignKey(Ligas, on_delete=models.SET_NULL,null=True,related_name='equipos_ligas')
    
    def __str__(self):
        return self.name

class Jugadores(models.Model):
    STATE_CHOICES = [
        ('del', 'Delantero'),
        ('def', 'Defensa'),
        ('med', 'Medio Campista'),
        ('ban_der', 'Banda Derecha'),
        ('ban_izq', 'Banda Izquierda'),
        ('por', 'Portero'),
        
    ]

    name = models.CharField(max_length=200)
    posicion = models.CharField(max_length=200,choices=STATE_CHOICES)
    num_player = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='jugadores/')
    equipo_id = models.ForeignKey(Equipos, on_delete=models.SET_NULL,null=True,related_name='jugadores_equipos')

    def __str__(self):
        return self.name
    


class Arbitros(models.Model):
    name = models.CharField(max_length=200)
    liga_id = models.ForeignKey(Ligas,on_delete=models.SET_NULL,null=True,related_name='arbitro_liga')
    foto = models.ImageField(upload_to='arbitros/')

    def __str__(self):
        return self.name


class Estadios(models.Model):
    name = models.CharField(max_length=200)
    liga_id = models.ForeignKey(Ligas, on_delete=models.SET_NULL,null=True,related_name='liga_estadio')
    foto = models.ImageField(upload_to='estadios/')

    def __str__(self):
        return self.name


class Eventos(models.Model):
    player_id = models.ForeignKey(Jugadores, on_delete=models.SET_NULL,null=True)
    tipo = models.CharField(max_length=200)
    minuto = models.CharField(max_length=200)
    tarjeta = models.CharField(max_length=200)


class Juegos(models.Model):
    STATE_CHOICES = [
        ('programado', 'Programado'),
        ('terminado', 'Terminado'),
    ]

    folio = models.CharField(max_length=200)
    fecha = models.DateField()
    liga_id = models.ForeignKey(Ligas, on_delete=models.SET_NULL,null=True)
    equipo1 = models.ForeignKey(Equipos, on_delete=models.SET_NULL,null=True,related_name='juegos_equipo1')
    equipo2 = models.ForeignKey(Equipos, on_delete=models.SET_NULL,null=True,related_name='juegos_equipo2')
    estadio = models.ForeignKey(Estadios, on_delete=models.SET_NULL,null=True)
    arbitro = models.ForeignKey(Arbitros,on_delete=models.SET_NULL,null=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='programado')
