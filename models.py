# -*- coding: utf-8 -*-

from lxml import etree
from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning, RedirectWarning

# mapping invoice type to journal type
TYPE2JOURNAL = {
    'out_invoice': 'sale',
    'in_invoice': 'purchase',
    'out_refund': 'sale_refund',
    'in_refund': 'purchase_refund',
}


class res_company(models.Model):
    _inherit = 'res.company'

    tuco_id = fields.Integer('Tuco ID')


class res_partner(models.Model):
    _inherit = 'res.partner'

    tuco_id = fields.Integer('Tuco ID')


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def _default_journal(self):
        res = super(AccountInvoice, self)._default_journal()
        inv_type = self._context.get('type', 'out_invoice')
        inv_types = inv_type if isinstance(inv_type, list) else [inv_type]
        company_id = self._context.get('company_id', self.env.user.company_id.id)
        domain = [
            ('type', 'in', filter(None, map(TYPE2JOURNAL.get, inv_types))),
            ('company_id', '=', company_id),
        ]
        journal_code = self._context.get('journal_code')
        note_journal = self.env.ref('odoo_publishers.sales_note_journal')
        if self._context.get('journal_type') == 'sale':
            if journal_code == 'Nota':
                return note_journal
            domain.append(('id', '!=', note_journal.id))
        return self.env['account.journal'].search(domain, limit=1)

    code = fields.Char(related='journal_id.code')
    journal_id = fields.Many2one(default=_default_journal)

    @api.multi
    def onchange_company_id(self, company_id, part_id, type, invoice_line, currency_id):
        res = super(AccountInvoice, self).onchange_company_id(company_id, part_id, type, invoice_line, currency_id)
        values = {}

        if company_id and type:
            journal_type = TYPE2JOURNAL[type]
            journal_code = self._context.get('journal_code')
            domain = [('type', '=', journal_type), ('company_id', '=', company_id)]
            if journal_type == 'sale':
                if journal_code == 'Nota':
                    domain.append(('code', '=', 'Nota'))
                else:
                    domain.append(('code', '!=', 'Nota'))
            journals = self.env['account.journal'].search(domain)
            if journals:
                values['journal_id'] = journals[0].id
            journal_defaults = self.env['ir.values'].get_defaults_dict('account.invoice', 'type=%s' % type)
            if 'journal_id' in journal_defaults:
                values['journal_id'] = journal_defaults['journal_id']
            if not values.get('journal_id'):
                field_desc = journals.fields_get(['type'])
                type_label = next(t for t, label in field_desc['type']['selection'] if t == journal_type)
                action = self.env.ref('account.action_account_journal_form')
                msg = _('Cannot find any account journal of type "%s" for this company, You should create one.\n Please go to Journal Configuration') % type_label
                raise RedirectWarning(msg, action.id, _('Go to the configuration panel'))
            domain = {'journal_id':  [('id', 'in', journals.ids)]}
            res.update({
                'domain': domain,
                'value': values
            })
        return res