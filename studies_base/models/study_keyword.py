# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyKeyword(models.Model):
    _name = "study.keyword"

    name = fields.Char("Name")
