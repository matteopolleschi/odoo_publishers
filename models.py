# -*- coding: utf-8 -*-

from openerp import models, fields, api


class res_company(models.Model):
    _inherit = 'res.company'

tuco_id = fields.Integer('Tuco ID')
