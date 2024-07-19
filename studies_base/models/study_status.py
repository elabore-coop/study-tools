# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyStatus(models.Model):
    _name = "study.status"

    name = fields.Char("Name")
    value = fields.Char("Value")
    sequence = fields.Integer("Sequence")

