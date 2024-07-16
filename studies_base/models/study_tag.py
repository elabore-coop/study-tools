# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyTag(models.Model):
    _name = "study.tag"

    name = fields.Char("Name")
