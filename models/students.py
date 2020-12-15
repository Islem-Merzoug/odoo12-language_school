from odoo import fields,models,api

class LanguageSchoolStudent(models.Model):
    _name = 'language_school.student'
    _description = 'Student'

    name = fields.Char(required=True)
    attendence = fields.Selection(string="Attendence",
                                  selection=[('present', 'Present'), ('absent', 'Absent')],
                                  required=False)
    lesson_id = fields.Many2one(comodel_name="language_school.lesson", string="lesson", required=False, )