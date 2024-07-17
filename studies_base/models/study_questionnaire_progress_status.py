# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyQuestionnaireProgressStatus(models.Model):
    _name = "study.questionnaire.progress.status"

    name = fields.Char("Name")
    value = fields.Char("Value")
    sequence = fields.Integer("Sequence")

