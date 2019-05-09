# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
import base64


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.multi
    def picking_state(self):
        for rec in self:
            rec.shipped = False
            if rec.picking_ids:
                picking_list = self.env['stock.picking'].search([
                                            ('id', 'in', rec.picking_ids.ids),
                                            ('state', '!=', 'done')])
                if not picking_list:
                    rec.shipped = True

    latitude = fields.Char('Latitude', copy=False)
    longitude = fields.Char('Longitude',  copy=False)
    cust_sign = fields.Binary('Customer Sign',  copy=False)
    cust_sign_name = fields.Char('Customer Sign Name', copy=False)
    shipped = fields.Boolean(compute='picking_state',string='Shipped')
    
    

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    prod_image = fields.Binary('Product Image',  copy=False)
    prod_img_name = fields.Char(' Received Product Image Name',  copy=False)
