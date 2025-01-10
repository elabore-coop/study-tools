# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyQuestionnaireResponse(models.Model):
    _name = "study.questionnaire.response"

    identifier_primary_id = fields.Char("Identifiant Seintinelles", readonly=True)
    progress_status = fields.Many2one("study.questionnaire.response.progress.status", string="État d'avancement")    
    authored = fields.Datetime("Date de saisie des réponses", readonly=True)
    
    identifier_author = fields.Char("ID plateforme", readonly=True)
    author = fields.Many2one("study.author", string="Platform d'étude", readonly=True)

    study_id = fields.Many2one("study.study", "Étude", readonly=True)
    study_questionnaire_id = fields.Many2one("study.questionnaire", string="Questionnaire", readonly=True)
    
    source = fields.Many2one("res.partner", string="Contact", domain=[("category_patient",'=',1)], readonly=True)
    firstname = fields.Char("Prénom", related="source.firstname")
    lastname = fields.Char("Nom", related="source.lastname")

    created = fields.Datetime("Date de création")
    updated = fields.Datetime("Date mise à jour")