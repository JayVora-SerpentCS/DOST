# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'DOST - Delivery Order, Signed and Tracked',
    'version': '8.0.0.1.0',
    'category': 'Sale',
    'summary': 'DOST - Delivery Order, Signed and Tracked',
    'description': """
    DOST - Delivery Order, Signed and Tracked
    """,
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'http://www.serpentcs.com',

    'depends': ['sale', 'web_tree_image', 'stock'],

    'data': [
        'views/sale_dost_view.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
