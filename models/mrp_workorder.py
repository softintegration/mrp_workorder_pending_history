# -*- coding: utf-8 -*- 

import datetime

from odoo import models, fields, api, _


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'


    pending_history_ids = fields.One2many('mrp.workorder.pending.history','workorder_id')

    def button_pending_wizard(self):
        workorder_pending_confirmation_wizard = self.env['mrp.workorder.pending.confirmation'].create({})
        return {
            'name': _('Pending confirmation'),
            'res_model': 'mrp.workorder.pending.confirmation',
            'view_mode': 'form',
            'context': {
                'active_model': 'mrp.workorder',
                'active_ids': self.ids,
            },
            'res_id': workorder_pending_confirmation_wizard.id,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }

    def button_pending_with_history(self,motif_id,date=False):
        for each in self:
            each._register_pending_history(motif_id,date=date)
        return self.button_pending()

    def _register_pending_history(self,motif_id,date=False):
        self.env['mrp.workorder.pending.history'].create(self._prepare_pending_history(motif_id,date=date))

    def _prepare_pending_history(self,motif_id,date=False):
        return {
            'workorder_id':self.id,
            'pending_motif':motif_id.name,
            'pending_motif_description':motif_id.description,
            'pending_date':date or fields.Datetime.now()
        }



class MrpWorkorderPendingMotif(models.Model):
    _name = 'mrp.workorder.pending.motif'

    name = fields.Char(string='Motif', required=True)
    description = fields.Text(string='Motif Detail')