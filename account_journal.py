import logging

from odoo import models

_logger = logging.getLogger(__name__)


class account_journal(models.Model):
    _inherit = "account.journal"

    def __init__(self, pool, cr):
        super(account_journal, self).__init__(pool, cr)
        cr.execute(
            "select prefix, suffix from ir_sequence where id in (select sequence_id from account_journal where code = 'SAJ') limit 1;")
        seq = cr.dictfetchone()
        if seq and (seq.get('prefix') is not None or seq.get('suffix') is None):
            cr.execute(
                "UPDATE ir_sequence SET suffix = '/%(year)s', prefix = null WHERE  id IN (SELECT sequence_id FROM   account_journal WHERE  code = 'SAJ');")
