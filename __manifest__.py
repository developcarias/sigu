# -*- coding: utf-8 -*-
{
    'name': 'sigu',
    'version': '1.1',
    'category': 'sigu',
    'summary': 'sigu',
    'description': "",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/curso_data.xml',  # Aquí es donde incluyes tu archivo de datos
        'views/curso_views.xml',
    ],
    'installable': True,
    'application': True,
}