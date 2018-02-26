# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from openerp import fields, models,api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    latitude = fields.Char('Latitude', copy=False)
    longitude = fields.Char('Longitude', copy=False)
    cust_sign = fields.Binary('Customer Sign', copy=False)
    cust_sign_name = fields.Char('Customer Sign Name', copy=False)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    prod_image = fields.Binary('Product Image', copy=False)
    prod_img_name = fields.Char('Product Image Name', copy=False)
