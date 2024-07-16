# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyQuestionnaireResponseProgressStatus(models.Model):
    _name = "study.questionnaire.response.progress.status"

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")

