# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def picking_state(self):
        for rec in self:
            shipped = False
            if rec.picking_ids:
                picking_list = self.env['stock.picking'].search([
                    ('id', 'in', rec.picking_ids.ids),
                    ('state', '!=', 'done')])
                if not picking_list:
                    shipped = True
            rec.shipped = shipped

    latitude = fields.Char('Latitude', copy=False)
    longitude = fields.Char('Longitude', copy=False)
    shipped = fields.Boolean(compute='picking_state')
    is_signed = fields.Boolean('Is signed', defualt=False)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    prod_image = fields.Binary('Product Image', copy=False)
    prod_img_name = fields.Char('Received Product Image Name', copy=False)
