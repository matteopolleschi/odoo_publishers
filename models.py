# -*- coding: utf-8 -*-

from openerp import models, fields, api


class res_company(models.Model):
    _inherit = 'res.company'

    tuco_id = fields.Integer('Tuco ID')

class res_partner(models.Model):
    _inherit = 'res.partner'

    tuco_id = fields.Integer('Tuco ID')
