# -*- coding: utf-8 -*-

from odoo import models, fields, api
class rooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'hotel room master list'


    name = fields.Char("Room No")
    description = fields.Char("Room Description")
    roomtype_id = fields.Many2one('hotel.roomtypes', string="Room Type")
    roomtypename = fields.Char("Room Type",related='roomtype_id.name')
    room_ids = fields.Char("Room ID", related= 'roomtype_id.name')