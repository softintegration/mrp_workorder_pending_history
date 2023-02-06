# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models,_
from odoo.exceptions import ValidationError


class MrpWorkorderPendingConfirmation(models.TransientModel):
    _name = 'mrp.workorder.pending.confirmation'
    _description = 'Pending confirmation'

    pending_date = fields.Datetime(string='Pending date', default=lambda self: fields.Datetime.now())
    pending_motif_id = fields.Many2one('mrp.workorder.pending.motif',string='Pending motif')


    def apply(self):
        if not self.pending_motif_id:
            raise ValidationError(_("Pending motif is required!"))
        mrp_workorder_ids = self.env.context.get("active_ids")
        mrp_workorders = self.env['mrp.workorder'].browse(mrp_workorder_ids)
        return mrp_workorders.button_pending_with_history(self.pending_motif_id,date=self.pending_date)




