# -*- coding: utf-8 -*-
{
    'name': "Odoo for Publishing",

    'summary': "Module for publishing businesses",

    'description': "Additional fields and VAT mapping",

    'author': "Daphne Solutions",
    'website': "http://www.github.com/matteopolleschi/odoo_imppn",
    'category': 'Accounting & Finance',
    'version': '0.1',

    'depends': ['web', 'base', 'account', 'account_accountant'],

    'data': [
        'views.xml',
        'data/account_data.xml',
    ],
}
