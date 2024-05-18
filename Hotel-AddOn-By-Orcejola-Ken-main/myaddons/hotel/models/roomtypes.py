# -*- coding: utf-8 -*-

#roomtypes.py

from odoo import models, fields, api

class roomtypes(models.Model):
    _name = 'hotel.roomtypes'
    _description = 'hotel roomtypes list'
    _order="name"

name = fields.Char("Room Name")
description = fields.Char("Room Description")
imageroom = fields.Image("Room")
imagebathroom = fields.Image("Bath Room")
charges_ids=fields.One2many('hotel.charges','roomtype_id', string=' Charges')


class charges(models.Model):
    _name = 'hotel.charges'
    _description = 'hotel roomtype  charges list'
    charge_id = fields.Many2one('hotel.charges',string="Charge Title")
    amount = fields.Float("Amount", digits=(10,2), options={'always_reload': True})
    roomtype_id = fields.Many2one('hotel.roomtypes', string="Room Type")