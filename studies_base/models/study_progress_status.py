# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyProgressStatus(models.Model):
    _name = "study.progress.status"

    _rec_name = 'state'

    study_id = fields.Many2one("study.study", string="Étude")
    state = fields.Selection([
        ('DRAFT', 'Brouillon'), 
        ('NOT-YET-RECRUITING', 'À venir'), 
        ('RECRUITING', 'En cours de recrutement'), 
        ('ACTIVE-BUT-NOT-RECRUITING', 'Active mais ne recrute plus'), 
        ('COMPLETED', 'Terminée'), 
        ('WITHDRAWN', 'Annulé')], string="Avancement de l'étude")
    actual = fields.Boolean("Statut actuel")
    date_begin = fields.Date("Date de début de l'état")
    date_end = fields.Date("Date de fin de l'état")