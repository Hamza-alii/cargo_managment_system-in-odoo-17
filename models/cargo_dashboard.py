from odoo import models, fields, api

class CargoDashboard(models.Model):
    _name = 'cargo.dashboard'
    _description = 'Cargo Dashboard'
    _rec_name = 'status'

    status = fields.Selection([
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered')
    ], string="Shipment Status", required=True, default='pending')

    total_shipments = fields.Integer(string="Total Shipments", compute="_compute_shipment_counts", store=True)
    pending_shipments = fields.Integer(string="Pending Shipments", compute="_compute_shipment_counts", store=True)
    delivered_shipments = fields.Integer(string="Delivered Shipments", compute="_compute_shipment_counts", store=True)

    total_weight = fields.Float(string="Total Weight (kg)", compute="_compute_shipment_counts", store=True)
    total_revenue = fields.Monetary(string="Total Revenue", compute="_compute_shipment_counts", store=True, currency_field="currency_id")

    currency_id = fields.Many2one('res.currency', string="Currency", default=lambda self: self.env.company.currency_id)

    @api.depends('status')
    def _compute_shipment_counts(self):
        """ Xisaabi xogta guud ee shixnadaha (shipments) """
        for record in self:git
            shipments = self.env['cargo.shipment'].search([('status', '=', record.status)])
            record.total_shipments = len(shipments)
            record.pending_shipments = len(shipments.filtered(lambda s: s.status == 'pending'))
            record.delivered_shipments = len(shipments.filtered(lambda s: s.status == 'delivered'))
            record.total_weight = sum(shipments.mapped('weight'))
            record.total_revenue = sum(shipments.mapped('price_total'))
