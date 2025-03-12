from odoo import models, fields, api
# ---------------------------
# Cargo Vehicle Model
# ---------------------------
class CargoVehicle(models.Model):
    _name = 'cargo.vehicle'
    _description = 'Cargo Vehicle'

    name = fields.Char(string='Vehicle Name', required=True)
    license_plate = fields.Char(string='License Plate', required=True)
    capacity = fields.Float(string='Capacity (kg)', required=True)
    active = fields.Boolean(string='Active', default=True)
    driver_id = fields.Many2one('cargo.employee', string='Assigned Driver')
