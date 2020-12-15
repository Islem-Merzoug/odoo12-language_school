# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LanguageSchoolClass(models.Model):
    ''' Defining a student information '''
    # _name = 'language_school.service'
    _inherit = 'product.template'
    _description = 'Service Information'

    is_service = fields.Boolean(string="Is a service", default='True')

    # teacher_id = fields.Many2one("res.partner", string="teacher", required=False)

    def get_default_service_type(self):
        return 'is_service' in self.env.context

    is_service = fields.Boolean(default=get_default_service_type)
    # type = fields.Selection(required=False)
    # type = fields.Selection(selection_add=[('b', 'B'), ('c', 'C')], default='b', )

