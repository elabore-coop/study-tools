# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyStudy(models.Model):

    _name = "study.study"

    title = fields.Char("Nom de l'étude")
    name = fields.Char("Acronyme")

    period_start = fields.Date("Début de l'étude")
    period_end = fields.Date("Fin de l'étude")
    progress_status_id = fields.Many2one("study.progress.status", string="Avancement de l'étude") #should be computed to actual progress status
    progress_status = fields.One2many("study.progress.status", "study_id", "All progress status")

    description_summary = fields.Char("Brève description de l'étude")
    description = fields.Text("Description de l'étude")
    keywords = fields.Many2many("study.keyword", string="Mots-clés")
    primary_purpose_type = fields.Many2one("study.purpose.type", string="Objectif principal")
    part_of = fields.Many2one("study.study", string="Fait partie de")
    version = fields.Char("Version")
    phase = fields.Many2one("study.phase", string="Phase")
    status = fields.Many2one("study.status", string="Status de la publication")

    site = fields.Many2one("res.partner", string="Lieu de l'étude")
    identitifer_author = fields.Char("ID plateforme")

    identifier_primary_id  = fields.Char("Idientifiant Seintinelles", readonly=True)

    recruitment_target_number = fields.Integer("Nombre de participants à recruter")
    recruitment_max_number = fields.Integer("Nombre limite de participations")
    recruitment_eligibility_gender = fields.Many2one("study.gender", string="Genre")
    recruitment_eligibility_age_min = fields.Integer("Âge min")
    recruitment_eligibility_age_max = fields.Integer("Âge max")
    recruitment_eligibility_condition_clinical_status = fields.Many2many("study.eligibility.condition.clinical.status", string="Statut de l'affectation (malade, ancien malade...)")
    recruitment_eligibility_condition_body_site = fields.Many2many("study.eligibility.condition.body.site", string="Localisation anatomique de l'affection")
    recruitment_eligibility_study_incl = fields.Many2many("study.study", 
                                                          "study_study_recruitment_eligibility_study_incl", 
                                                          "base_study_id", 
                                                          "incl_study_id", 
                                                          string="Doit avoir participé aux études...")
    recruitment_eligibility_study_excl = fields.Many2many("study.study", 
                                                          "study_study_recruitment_eligibility_study_excl", 
                                                          "base_study_id", 
                                                          "excl_study_id", 
                                                          string="Ne doit pas avoir participé aux études...")
    recruitment_eligibility_description = fields.Text("Description de la cible")
    recruitment_eligibility_topic = fields.Many2many("study.eligibility.topic", string="Thématique de recherche")
    region = fields.Many2many("study.region", string="Zones géographiques étudiées")
    

    note = fields.Text("Annotations")

    created = fields.Datetime('Created')
    updated = fields.Datetime('Updated')