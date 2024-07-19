# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyEligibilityTopic(models.Model):
    _name = "study.eligibility.topic"

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")
    value = fields.Char("Value")

