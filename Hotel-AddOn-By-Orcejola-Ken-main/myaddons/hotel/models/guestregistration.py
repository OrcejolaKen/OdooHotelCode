#Guest Registration Model

# -*- coding: utf-8 -*-

#guestregistration.py

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class guestregistration(models.Model):
    _name = 'hotel.guestregistration'
    _description = 'hotel guest registration list'

    room_id = fields.Many2one("hotel.rooms", string="Room No.")
    guest_id = fields.Many2one("hotel.guests", string="Guest Name")

     #roomname -< related fields found in the model hotel.rooms    
    roomname=fields.Char("Room Number.",related='room_id.name')

     #roomtname <- room type name found in the model hotel.rooms 
     # also related to hotel.roomtypes
    roomtypename=fields.Char("Room Type",related='room_id.roomtypename')

     #guestname <- related field found as a computed field called name in 
     #the model hotel.guests
    
    guestname=fields.Char("Guest Name",related='guest_id.name')
    datecreated = fields.Date("Date Created", default=lambda self: fields.Date.today())
    datefromSched = fields.Date("Scheduled Check In")
    datetoSched = fields.Date("Scheduled Check Out")
    datefromAct = fields.Date("Actual Check In")
    datetoAct = fields.Date("Actual Check Out")
    #computed field called name <- concatenation of room name and guest name
    name= fields.Char("Guest Registration",compute='_compute_name',store=False)

    @api.depends('room_id', 'guest_id')
    def _compute_name(self):
            for rec in self:
                rec.name= f"{rec.roomname}, {rec.guestname}"
                
    state = fields.Selection([
            ('DRAFT','Draft'),
            ('NOW CHECKEDIN','Checked In'),
            ('NOW CHECKEDOUT','Checked Out'),
            ('NOW CANCELLED','Cancelled')],
            string="Status", default="DRAFT")

    def action_reserve(self):
        for rec in self:
            if not(rec.guest_id):
                    raise ValidationError('Please enter a valid guest name.')
            elif not(rec.roomname):
                    raise ValidationError('Please enter a valid Room Number.')
            else:
                rec.state= "NOW RESERVED"

    def action_checkin(self):
        for rec in self:
            if not(rec.guest_id):
                    raise ValidationError('Please enter a valid guest name.')
            elif not(rec.roomname):
                    raise ValidationError('Please enter a valid Room Number.')
            else:
                rec.state= "NOW CHECKED IN"

    def action_checkout(self):
        for rec in self:
            if not(rec.guest_id):
                    raise ValidationError('Please enter a valid guest name.')
            elif not(rec.roomname):
                    raise ValidationError('Please enter a valid Room Number.')
            else:
                rec.state= "NOW CHECKED OUT"

    def action_cancel(self):
        for rec in self:
            if not(rec.guest_id):
                    raise ValidationError('Please enter a valid guest name.')
            elif not(rec.roomname):
                    raise ValidationError('Please enter a valid Room Number.')
            else:
                rec.state= "NOW CANCELLED"