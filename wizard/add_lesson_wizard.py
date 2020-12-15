# -*- coding: utf-8 -*-
from odoo import models, fields, api
import dateutil.relativedelta as relativedelta
import dateutil.rrule as rrule
import datetime


class AddLessonWizard(models.Model):
    _name = 'language_school.lesson_wizard'
    _description = 'Add lessons'

    student_ids = fields.Many2many('language_school.student', string="Students")

    @api.multi
    def add_lesson(self):
        self.ensure_one()
        classes = self.env['language_school.class'].browse(self.env.context.get('active_ids'))
        print(classes)
        for record in classes:
            # print(record)
            weekdays = ()
            duration = (datetime.timedelta(hours=record.date_end.hour, minutes=record.date_end.minute, seconds=record.date_end.second) -
                        datetime.timedelta(hours=record.date_start.hour, minutes=record.date_start.minute, seconds=record.date_start.second))

            service = record.service_id
            teacher = record.teacher_id
            student = record.student_idss

            # daily
            if record.repeat == 'daily':
                # On peut spécifier directement la date de fin à l'aide du paramètre `until`
                dates = rrule.rrule(rrule.DAILY, dtstart=record.date_start, until=record.date_end)

            # weekly
            elif record.repeat == 'weekly':
                if record.monday:
                    weekdays += (relativedelta.MO,)
                if record.tuesday:
                    weekdays += (relativedelta.TU,)
                if record.wednesday:
                    weekdays += (relativedelta.WE,)
                if record.thursday:
                    weekdays += (relativedelta.TH,)
                if record.friday:
                    weekdays += (relativedelta.FR,)
                if record.saturday:
                    weekdays += (relativedelta.SA,)
                if record.sunday:
                    weekdays += (relativedelta.SU,)
                print('weekdays:' ,weekdays)

                rr = rrule.rrule(rrule.WEEKLY, byweekday=weekdays, dtstart=record.date_start)
                print('rr:' ,rr)
                dates = rr.between(record.date_start, record.date_end, inc=True)

                print('dates:' ,dates)

            # monthly
            elif record.repeat == 'monthly':
                rr = rrule.rrule(rrule.MONTHLY, dtstart=record.date_start, until=record.date_end)
                dates = rr.between(record.date_start, record.date_end, inc=True)


            if dates:
                lines = [(0, 0, {'name': record.name, 'date_start': date, 'date_end': date + duration, 'service_id': service.id, 'teacher_id': teacher.id, 'student_ids': [(6, 0, student.ids)]})
                         for date in dates]

                record.write({'lesson_ids': lines })
                # record.write({'lesson_ids': lines, 'student_ids': [(6, 0, student.ids)]})
                # lessons = self.env['language_school.lesson']
                # for lesson in lessons:
                #     lesson.write({'service_id': [(6, 0, self.service_id.id)]})


        return True