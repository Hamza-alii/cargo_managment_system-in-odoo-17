from odoo import models, fields, api
# ---------------------------
# Cargo Employee Model
# ---------------------------
class CargoEmployee(models.Model):
    _name = 'cargo.employee'
    _description = 'Cargo Employee'

    name = fields.Char(string='Employee Name', required=True)
    job_position = fields.Selection([
        ('driver', 'Driver'),
        ('manager', 'Manager'),
        ('staff', 'Staff')
    ], string='Job Position', required=True)
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    active = fields.Boolean(string='Active', default=True)