# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'DOST - Delivery Order, Signed and Tracked',
    'summary': 'This module presents a delivery boy-friendly mobile app working with Odoo. The application helps the delivery boy get the order confirmed, signed, and tracked, and the data is sent to the server.',
    'description': """
		This module presents a delivery boy-friendly mobile app working with Odoo. The application helps the delivery boy get the order confirmed, signed, and tracked, and the data is sent to the server.
		DOST - Delivery Order, Signed and Tracked
		Delivery Order, Signed and Tracked
		Odoo Delivery Order, and Tracked
		Delivery Order, and Tracked in odoo
		Delivery Order, Signed and Tracked app
		Odoo signed and tracked app
    """,
    'version': '18.0',
    'category': 'Sale',
    'license': 'LGPL-3',
    'live_test_url': 'https://youtu.be/roZbXESyhhg',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',

    'depends': ['stock', 'sale_management'],

    'data': [
        'views/sale_dost_view.xml',
    ],
    'application': False,
    'images': ['static/description/Banner_sale_dost.png'],
    "live_test_url": "https://www.youtube.com/watch?v=roZbXESyhhg",
    'price': '59',
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
}
