# -*- coding: utf-8 -*-

{
    'name': 'Hospital managment',
    'sequence': -100,
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Amir',
    'application': True,
    'summary': 'Hospital managment system',
    'description': """This module contains all the common features of Hospital Management.""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,    
    'license': 'LGPL-3',
}
