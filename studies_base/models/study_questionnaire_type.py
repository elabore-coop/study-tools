# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyQuestionnaireType(models.Model):
    _name = "study.questionnaire.type"

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")

