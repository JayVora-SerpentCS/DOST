# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'DOST - Delivery Order, Signed and Tracked',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'license': 'LGPL-3',
    'live_test_url': 'https://youtu.be/roZbXESyhhg',
    'summary': 'DOST - Delivery Order, Signed and Tracked',
    'description': """
    DOST - Delivery Order, Signed and Tracked
    """,
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'http://www.serpentcs.com',

    'depends': ['sale_management', 'stock',],

    'data': [
        'views/sale_dost_view.xml',
    ],
    'application': False,
    'images': ['static/description/banner_DOST.jpg'],    
    'price': '39',
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
}
