# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyQuestionnaireStatus(models.Model):
    _name = "study.questionnaire.status"

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")

