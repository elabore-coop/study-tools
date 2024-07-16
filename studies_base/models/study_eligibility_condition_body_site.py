# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyEligibilityConditionBodySite(models.Model):
    _name = "study.eligibility.condition.body.site"

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")

