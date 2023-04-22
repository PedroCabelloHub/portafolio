from odoo import models, fields, api

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    name = fields.Char(string='Numero de habitación')
    tipo_de_habitacion = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')
    ], string='Tipo de Habitación', required=True)
    precio_por_noche = fields.Float(string='Precio por Noche', required=True)
    estado = fields.Selection([
        ('available', 'Disponible'),
        ('occupied', 'Ocupada'),
        ('maintenance', 'Mantenimiento')
    ], string='Estado',default='available')

    @api.onchange('tipo_de_habitacion')
    def onchange_tipo_de_habitacion(self):
        if self.tipo_de_habitacion == 'single':
            self.precio_por_noche = 400.0
        elif self.tipo_de_habitacion == 'double':
            self.precio_por_noche = 650.0
        elif self.tipo_de_habitacion == 'suite':
            self.precio_por_noche = 120.0
            
            
    def onchange_habilitar(self):
        self.estado = 'available'
            