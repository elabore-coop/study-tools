# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyQuestionnaire(models.Model):
    _name = "study.questionnaire"

    title = fields.Char("Nom du questionnaire")
    name = fields.Char("Acronyme")

    approval_date = fields.Datetime("Date d'approbation")
    last_review_date = fields.Datetime("Dernière relecture")
    effective_period_start = fields.Datetime("Début de la collecte")
    effective_period_end = fields.Datetime("Fin de la collecte")

    purpose = fields.Text("Objectif")
    subject_type = fields.Many2one("study.questionnaire.subject.type", string="Sujets")
    description = fields.Text("Description du questionnaire")

    jurisdiction = fields.Many2many("study.region", string="Zones géographiques ciblées")
    derived_from = fields.Many2one("study.questionnaire", string="Dérivé de")
    version = fields.Char("Vestion")
    status = fields.Many2one("study.questionnaire.status", string="Statut de publication")

    experimental = fields.Boolean("Questionnaire de test")
    identifier_author = fields.Char("ID plateforme")
    identifier_primary_id = fields.Char("Identifiant Seintinelles", readonly=True)

    copyright = fields.Text("Copyright")
    copyright_label = fields.Char("Propriétaire et année du copyright")