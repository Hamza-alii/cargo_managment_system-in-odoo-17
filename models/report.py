from odoo import models, fields, api
# ---------------------------
# Cargo Report Model
# ---------------------------
class CargoReport(models.AbstractModel):
    _name = 'report.cargo_management.report_shipment'
    _description = 'Cargo Shipment Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['cargo.shipment'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'cargo.shipment',
            'docs': docs,
        }