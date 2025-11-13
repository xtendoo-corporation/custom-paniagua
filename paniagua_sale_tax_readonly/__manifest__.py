{
    'name': 'Paniagua - Control de Impuestos Adicionales en Ventas',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Restringir edición de impuestos adicionales en líneas de venta',
    'author': 'Xtendoo',
    'website': 'https://www.xtendoo.es',
    'license': 'AGPL-3',
    'depends': ['sale', 'account'],
    'data': [
        'security/security.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}

