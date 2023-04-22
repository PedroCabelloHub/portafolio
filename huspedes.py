from odoo import models, fields

class HotelGuest(models.Model):
    _name = 'hotel.guest'
    _description = 'Hotel Guest'

    name = fields.Char(string='Nombre')
    last_name = fields.Char(string='Apellido')
    phone_number = fields.Char(string='Número de Teléfono')
    email = fields.Char(string='Correo Electrónico')
    check_in_date = fields.Date(string='Fecha de Ingreso')
    check_out_date = fields.Date(string='Fecha de Salida')
    