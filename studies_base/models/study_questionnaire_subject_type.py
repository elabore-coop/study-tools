# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyQuestionnaireSubjectType(models.Model):
    _name = "study.questionnaire.subject.type"

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")
    value = fields.Char("Value")

