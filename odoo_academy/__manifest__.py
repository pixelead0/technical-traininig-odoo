# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',

    'description': """
        Academy module to manage Training
    """,
    'author': 'IINGEN',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '0.1',
    'depends': ['base', 'sale'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitem.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}
