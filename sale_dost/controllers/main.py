# -*- coding: utf-8 -*

import logging
from odoo import http
from odoo.http import request
_logger = logging.getLogger(__name__)


class UsersLogin(http.Controller):

    @http.route(['/web/delivery_reset_password'], auth='public', type='json')
    def web_delivery_reset_password(self, **kw):
        res = {'reset_result': False, 'disp_msg':''}
        if kw and kw.get('args') and kw.get('args')[0]:
            records = kw.get('args')[0]
            if records and records.get('login'):
                login = records.get('login')
                user_rec = request.env['res.users'].sudo().search([
                    ('login', '=', str(login))], limit=1)
                if user_rec and user_rec.id:
                    user_rec.sudo().action_reset_password()
                    res['reset_result'] = True
                    res['disp_msg'] = 'Password reset link has been ' \
                                      'successfully sent in your email id'
                else:
                    res['disp_msg'] = 'No user found with this login id'
        return res
