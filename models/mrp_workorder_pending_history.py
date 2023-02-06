# -*- coding: utf-8 -*- 

import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from odoo.tools import float_compare, float_round, float_is_zero
from odoo.tools import format_datetime


class MrpWorkorderPendingHistory(models.Model):
    """ Manufacturing Orders request"""
    _name = 'mrp.workorder.pending.history'
    _description = 'Workorder pending history'
    _order = 'create_date DESC'

    workorder_id = fields.Many2one('mrp.workorder', required=True, ondelete='cascade')
    pending_motif = fields.Char(string='Motif', required=True)
    pending_motif_description = fields.Char(string='Motif details')
    pending_date = fields.Datetime(string='Pending date', default=lambda self: fields.Datetime.now(),
                                       required=True)

    def name_get(self):
        res = []
        for pending_history in self:
            res.append((pending_history.id, '%s (%s)' % (
            pending_history.workorder_id.name, pending_history.pending_motif)))
        return res