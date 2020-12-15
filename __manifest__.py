# -*- coding: utf-8 -*-
{
    'name': "language_school",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['portal',
                'product',
                'purchase'
                ],

    # always loaded
    'data': [
        'views/classes.xml',
        'views/lessons.xml',
        'views/services.xml',
        'views/menus.xml',
        'security/ir.model.access.csv',
        'wizard/add_lesson_wizard_view.xml',
        'data/data.xml',
        'reports/report.xml',
        'reports/class_invoice.xml',
    ],
}