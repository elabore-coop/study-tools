# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyQuestionnaire(models.Model):
    _name = "study.questionnaire"

    title = fields.Char("Nom du questionnaire")
    name = fields.Char("Acronyme")

    progress_status = fields.Many2one("study.progress.status", string="Statut du questionnaire")
    approval_date = fields.Datetime("Date d'approbation")
    last_review_date = fields.Datetime("Dernière relecture")
    effective_period_start = fields.Datetime("Début de la collecte")
    effective_period_end = fields.Datetime("Fin de la collecte")

    study_id = fields.Many2one("study.study", string="Étude")
    category = fields.Many2one("study.questionnaire.category", string="Catégorie de questionnaire")
    type = fields.Many2one("study.questionnaire.type", string="Type de questionnaire")
    purpose = fields.Text("Objectif")
    subject_type = fields.Many2one("questionnaire.subject.type", string="Sujets")
    description = fields.Text("Description du questionnaire")

    jurisdiction = fields.Many2many("study.region", string="Zones géographiques ciblées")
    derived_from = fields.Many2one("study.questionnaire", string="Dérivé de")
    version = fields.Char("Vestion")
    status = fields.Many2one("study.questionnaire.status", string="Statut de publication")

    experimental = fields.Boolean("Questionnaire de test")
    author = fields.Many2one("study.author", string="Platforme d'étude")
    identifier_author = fields.Char("ID plateforme")
    identifier_primary_id = fields.Char("Identifiant Seintinelles", readonly=True)

    rank_in_study = fields.Integer("Rang dans l'étude")
    fixed_start_date = fields.Datetime("Date de début de collecte")
    fixed_end_date = fields.Datetime("Date limite de collecte")
    repeated = fields.Integer("Nombre de répétition")
    repeat_delay = fields.Integer("Délai de répétition")
    repeat_delay_type = fields.Selection([("d", "Jour"), ("m", "Mois"), ("y", "Année")], string="Type de délai de répétition")
    following = fields.Many2one("study.questionnaire", string="Questionnaire précédent")
    following_repeat_delay = fields.Integer("Délai avec le questionnaire précédent")
    following_repeat_delay_type = fields.Selection([("d", "Jour"), ("m", "Mois"), ("y", "Année")], string="Type de délai avec le questionnaire précédent")
    preceding = fields.Many2one("study.questionnaire", string="Questionnaire suivant")
    preceding_repeat_delay = fields.Integer("Délai avec le questionnaire suivant")
    preceding_repeat_delay_type = fields.Selection([("d", "Jour"), ("m", "Mois"), ("y", "Année")], string="Type de délai avec le questionnaire suivant")

    copyright = fields.Text("Copyright")
    copyright_label = fields.Char("Propriétaire et année du copyright")