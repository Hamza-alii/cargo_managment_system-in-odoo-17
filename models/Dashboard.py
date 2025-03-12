from odoo import models, fields, api
# ---------------------------
# Dashboard Model
# ---------------------------
class CargoDashboard(models.Model):
    _name = 'cargo.dashboard'
    _description = 'Cargo Management Dashboard'

    total_shipments = fields.Integer(string='Total Shipments', compute='_compute_total_shipments')
    pending_shipments = fields.Integer(string='Pending Shipments', compute='_compute_pending_shipments')
    delivered_shipments = fields.Integer(string='Delivered Shipments', compute='_compute_delivered_shipments')

    @api.depends()
    def _compute_total_shipments(self):
        self.total_shipments = self.env['cargo.shipment'].search_count([])

    @api.depends()
    def _compute_pending_shipments(self):
        self.pending_shipments = self.env['cargo.shipment'].search_count([('status', '=', 'pending')])

    @api.depends()
    def _compute_delivered_shipments(self):
        self.delivered_shipments = self.env['cargo.shipment'].search_count([('status', '=', 'delivered')])
