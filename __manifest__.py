# -*- coding: utf-8 -*-
{
    'name': "Odoo for Publishing",

    'summary': "Module for publishing businesses",

    'description': "Additional fields and VAT mapping",

    'author': "Daphne Solutions",
    'website': "https://github.com/matteopolleschi/odoo_publishers",
    'category': 'Accounting & Finance',
    'version': '1.0',
    'depends': ['web', 'base', 'account'],
    'data': [
        'views.xml',
        'data/account_data.xml',
        'report/inherit_account_report.xml',
    ],
}
