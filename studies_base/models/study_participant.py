# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyParticipant(models.Model):
    _name = "study.participant"

    identifier_primary_id = fields.Char("Idientifiant Seintinelles", readonly=True)
    part_of = fields.Many2one("study.study", string="Étude", readonly=True)

    subject = fields.Many2one("res.partner", string="Contact", domain=[("category_patient",'=',1)], readonly=True)
    firstname = fields.Char("Prénom", related="subject.firstname")
    lastname = fields.Char("Nom", related="subject.lastname")
    progress_status = fields.Many2one("study.participant.progress.status", string="Statut de la participation")
    state = fields.Many2one("study.participant.state", string="État de la participation")

    part_of_author = fields.Many2one("study.author", string="Platforme d'étude", related="part_of.author")
    author = fields.Char("ID plateforme")
    identifier = fields.Char("Idientifiants de l'enrôlement")

    #questionnaire_responses = fields.One2many("study.questionnaire.response", "study_questionnaire_id", string="Réponses")
