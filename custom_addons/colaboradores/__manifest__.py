# -*- coding: utf-8 -*-
{
    'name': 'Colaboradores',
    'version': '1.0',
    'author': 'Tu Nombre',
    'category': 'Human Resources',
    'application': True,
    'summary': 'Registro de colaboradores simples',
    'depends': ['base'],     # requiere el módulo base de Odoo
    'data': [
        
        'views/colaboradores_views.xml',
        'views/colaboradores_menu.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            '/colaboradores/static/src/css/colaboradores.css',
        ],
    },
    'installable': True,
    'application': True,
}
