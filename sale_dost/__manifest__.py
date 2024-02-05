# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'DOST - Delivery Order, Signed and Tracked',
    'version': '13.0.1.0.0',
    'category': 'Sale',
    'license': 'LGPL-3',
    'summary': 'DOST - Delivery Order, Signed and Tracked',
    'description': """
    DOST - Delivery Order, Signed and Tracked
    """,
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'http://www.serpentcs.com',

    'depends': ['stock', 'sale_management'],

    'data': [
        'views/sale_dost_view.xml',
    ],
    'application': False,
    'price': '39',
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
}
