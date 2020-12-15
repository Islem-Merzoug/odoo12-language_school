# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LanguageSchoolLesson(models.Model):
    _name = 'language_school.lesson'
    _description = 'Lesson'

    name = fields.Char(required='True')
    date_start = fields.Datetime()
    date_end = fields.Datetime()
    state = fields.Selection([('draft', 'Draft'), ('completed', 'Completed')], default='draft')

    service_id = fields.Many2one("product.product", string="Service", required=False)
    teacher_id = fields.Many2one("res.users", string="Teacher", required=False)

    # student_ids = fields.Many2many('language_school.student', string="Students", required=False)
    student_ids = fields.One2many('language_school.student', 'lesson_id', string="student")

    # partent_id = fields.Many2many('language_school.student', 'Parent Product', ondelete='cascade'),
    # product_ids = fields.One2many('language_school.student', 'parent_id', 'Products'),

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
    # @api.depends('student_ids')
    def set_to_started(self):
        self.ensure_one()
        self.write({'state': 'started'})
        lessons = self.env['language_school.lesson'].browse(self.env.context.get('active_ids'))
        print(lessons)
        for lesson in lessons:
            print(lesson)
            # lesson.student_ids.write({'attendence': 'present'})
        return True

    @api.multi
    def add_lesson(self):
        self.ensure_one()
        # active_ids = self.env.context.get('active_ids')
        active_ids = self.env['language_school.student'].browse(self.env.context.get('active_ids'))
        print(active_ids)

    @api.multi
    def set_to_completed(self):
        self.write({'state': 'completed'})
        return True

    @api.multi
    def set_to_canceled(self):
        self.write({'state': 'canceled'})
        return True



    # @api.multi
    # @api.depends('student_ids')
    # def set_to_started(self):
    #     self.write({'state': 'started'})
    #     x = range(len(self.student_ids))
    #     for student in x:
    #         student.write({'attendence': 'present'})
    #     return True



    # @api.multi
    # def set_to_started(self):
    #     self.write({'state': 'started'})
    #     # students = self.env['language_school.student'].browse(self.env.context.get('active_ids'))
    #
    #     return True