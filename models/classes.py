# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _


class LanguageSchoolClass(models.Model):
    _name = 'language_school.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Class'

    name = fields.Char()

    date_start = fields.Datetime(string='From')
    date_end = fields.Datetime(string='To')

    service_id = fields.Many2one("product.product", string="Service", required=False)
    teacher_id = fields.Many2one("res.users", string="Teacher", required=False)

    localisation = fields.Selection(string="Localisation",
                                    selection=[('salle1', 'Salle1'), ('salle2', 'Salle2'), ('salle3', 'Salle3'), ],
                                    required=False)

    availisable_space = fields.Integer(string="", required=False)

    student_idss = fields.Many2many('language_school.student', string="Students")

    repeat = fields.Selection([('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], string="Repeats")

    monday = fields.Boolean()
    tuesday = fields.Boolean()
    wednesday = fields.Boolean()
    thursday = fields.Boolean()
    friday = fields.Boolean()
    saturday = fields.Boolean()
    sunday = fields.Boolean()

    lesson_ids = fields.Many2many('language_school.lesson', string="Lessons")

    nbr_lessons = fields.Integer(string="nombre de lessons", compute='number_lessons', required=False, )

    state = fields.Selection([('draft', 'Draft'),
                              ('started', 'Started'),
                              ('completed', 'Completed'),
                              ('canceled', 'Canceled')], 'State',
                             readonly=True, default='draft')

    @api.multi
    def set_to_draft(self):
        self.write({'state': 'draft'})
        return True

    @api.multi
    def set_to_started(self):
        self.write({'state': 'started'})
        return True

    @api.multi
    def set_to_completed(self):
        self.write({'state': 'completed'})
        return True

    @api.multi
    def set_to_canceled(self):
        self.write({'state': 'canceled'})
        return True


    @api.multi
    def add_lessons(self):
        form_view = self.env.ref('language_school.add_lesson_wizard_form')
        return {
            'name': _('Add Lessons'),
            'type': 'ir.actions.act_window',
            'res_model': 'language_school.lesson_wizard',
            'view_type': 'form',
            'view_mode': 'form',
            'views': [(form_view.id, 'form')],
            'view_id': form_view.id,
            'target': 'new'
        }

    @api.depends('lesson_ids')
    def number_lessons(self):
        for lesson in self:
            lesson.nbr_lessons = len(lesson.lesson_ids)

class Localisation(models.Model):
    ''' Defining a classe localisation '''
    _name = 'language_school.class.localisation'
    _description = 'classe localisation Information'

    name = fields.Char(string="Name", required=True)

