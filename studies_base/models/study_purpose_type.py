# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyPurposeType(models.Model):
    _name = "study.purpose.type"

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")

