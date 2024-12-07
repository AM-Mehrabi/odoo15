# -*- coding: utf-8 -*-

{
    'name': 'Complaint Management',
    'sequence': -100,
    'version': '1.0.0',
    'category': 'Management',
    'author': 'Amir',
    'application': True,
    'summary': 'Complaint management',
    'description': """This module handles the registration and management of complaints and suggestions for various ministries.""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/complaint_views.xml',
        'views/ministry_views.xml',
        'views/institution_views.xml',
        'views/suggestion_views.xml',
        'views/menu.xml',
    ],
    'web_icon' : '/Users/amir/Downloads/programming/Odoo/odoo-tutorial-project/odoo-15.0/app-odoo/om_complaints/static/description/complaint.png',
    'sequence' : -100,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
