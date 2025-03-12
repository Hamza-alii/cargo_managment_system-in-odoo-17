from odoo import models, fields, api

# ---------------------------
# Cargo Shipment Model
# ---------------------------
class CargoShipment(models.Model):
    _name = 'cargo.shipment'
    _description = 'Cargo Shipment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Shipment Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('cargo.shipment'))
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    vehicle_id = fields.Many2one('cargo.vehicle', string='Vehicle', required=True)
    employee_id = fields.Many2one('cargo.employee', string='Assigned Employee', required=True)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='pending', tracking=True)
    weight = fields.Float(string='Weight (kg)', required=True)
    delivery_date = fields.Date(string='Expected Delivery Date', required=True)
    actual_delivery_date = fields.Date(string='Actual Delivery Date')
    total_cost = fields.Float(string='Total Cost', compute='_compute_total_cost', store=True)
    note = fields.Text(string='Additional Notes')

    @api.depends('weight')
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = record.weight * 2.5  # Example cost calculation
