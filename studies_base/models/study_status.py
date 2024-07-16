# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudStatus(models.Model):
    _name = "study.status"

    name = fields.Char("Name")
    sequence = fields.Integer("Sequence")

