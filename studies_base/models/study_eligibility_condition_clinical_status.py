# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyEligibilityConditionClinicalStatus(models.Model):
    _name = "study.eligibility.condition.clinical.status"

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")
    value = fields.Char("Value")

