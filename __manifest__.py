# -*- coding: utf-8 -*-
{
    'name': "Odoo for Publishing",

    'summary': """Module for publishing businesses""",

    'description': """Additional fields and VAT mapping""",

    'author': "Daphne Solutions",
    'website': "https://github.com/matteopolleschi/odoo_publishers",

    'category': 'Accounting & Finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web', 'base', 'account', 'account_accountant'],

    # always loaded
    'data': [
        'views.xml',
        'data/account_data.xml',
        'report/inherit_account_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}