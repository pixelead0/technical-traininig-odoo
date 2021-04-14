# -*- coding: utf-8 -*-
{
    'name':'Odoo Academy',

    'description':"""
        Academy module to manage Training
    """,
    'author':'IINGEN',
    'website':'https://www.odoo.com',
    'category':'Training',
    'version':'0.1',
    'dependes':['base'],
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo':[
        'demo/academy_demo.xml',
    ],
}
