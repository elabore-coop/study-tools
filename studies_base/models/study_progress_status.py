# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyProgressStatus(models.Model):
    _name = "study.progress.status"

    