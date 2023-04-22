from odoo import models, fields, api

class HotelReservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Hotel Reservation'
    
    reservation_id = fields.Many2one('hotel.reservation')
    guest_id = fields.Many2one('hotel.guest', string='Huésped')
    room_id = fields.Many2one('hotel.room', string='Habitación')
    precio_por_noche = fields.Float(string='Precio por noche', compute='_compute_price_per_night')
    check_in_date = fields.Date(string='Fecha de Ingreso')
    noches = fields.Char(string='Numero de noches')
    check_out_date = fields.Date(string='Fecha de Salida')
    status = fields.Selection([
        ('available', 'Disponible'),
        ('occupied', 'Ocupada'),
        ('maintenance', 'Mantenimiento')
    ], string='Estado',default='available', compute='_compute_status')
    precio_total = fields.Float(String='Precio Total')
    

    #cambiar las fechas para el huesped desde otro evento
    def onchange_room_id(self):
        if self.room_id:
            self.room_id.write({'estado': 'occupied'})
            self.status = 'occupied'
        if self.guest_id:
            self.guest_id.write({'check_in_date': self.check_in_date})
            self.guest_id.write({'check_out_date': self.check_out_date})
        nights = (self.check_out_date - self.check_in_date).days
        self.write({'noches':nights})
        self.precio_total = self.room_id.precio_por_noche * nights    
            
    
    def onchange_desocupar(self):
        if self.room_id:
            self.room_id.write({'estado': 'maintenance'})
            self.status = 'maintenance'
        if self.guest_id:
            self.guest_id.unlink()
            self.guest_id.write({'active':False})
        self.reservation_id.unlink()
        self.reservation_id.write({'active':False})
            
    @api.depends('room_id')
    def _compute_price_per_night(self):
        for reservation in self:
            reservation.precio_por_noche = reservation.room_id.precio_por_noche
            
    @api.depends('room_id')
    def _compute_status(self):
        for reservation in self:
            reservation.status = reservation.room_id.estado
           
   