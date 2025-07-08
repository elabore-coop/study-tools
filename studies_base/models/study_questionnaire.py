# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StudyQuestionnaire(models.Model):
    _name = "study.questionnaire"

    title = fields.Char("Nom du questionnaire")
    name = fields.Char("Acronyme")

    approval_date = fields.Datetime("Date d'approbation")
    last_review_date = fields.Datetime("Dernière relecture")
    effective_period_start = fields.Datetime("Début de la collecte")
    effective_period_end = fields.Datetime("Fin de la collecte")

    purpose = fields.Text("Objectif")
    subject_type = fields.Many2many("study.questionnaire.subject.type", string="Sujets")
    description = fields.Text("Description du questionnaire")

    jurisdiction = fields.Many2many(
        "study.region", string="Zones géographiques ciblées"
    )
    derived_from = fields.Many2one("study.questionnaire", string="Dérivé de")
    version = fields.Char("Version")
    status = fields.Many2one(
        "study.questionnaire.status", string="Statut de publication"
    )

    experimental = fields.Boolean("Questionnaire de test")
    identifier_author = fields.Char("ID plateforme")
    identifier_primary_id = fields.Char("Identifiant Seintinelles", readonly=True)

    copyright = fields.Text("Copyright")
    copyright_label = fields.Char("Propriétaire et année du copyright")

    created = fields.Datetime("Created", compute="_compute_created", readonly=True)
    date = fields.Datetime("Date", compute="_compute_updated", readonly=True)

    @api.depends("create_date")
    def _compute_created(self):
        for record in self:
            if not record.created:
                record.created = record.create_date

    @api.depends("write_date")
    def _compute_updated(self):
        for record in self:
            record.date = record.write_date

    active = fields.Boolean("Actif", default=True)

    def copy(self, default=None):
        default = dict(default or {}, identifier_primary_id=None)
        return super().copy(default)

    @api.depends("title", "name")
    def name_get(self):
        result = []
        for questionnaire in self:
            if not questionnaire.name:
                result.append((questionnaire.id, questionnaire.title))
            else:
                result.append(
                    (questionnaire.id, f"[{questionnaire.name}] {questionnaire.title}")
                )
        return result
