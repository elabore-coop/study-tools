# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo import osv
from odoo.exceptions import UserError


class StudyQuestionnaireResponse(models.Model):
    _name = "study.questionnaire.response"

    identifier_primary_id = fields.Char("Idientifiant Seintinelles", readonly=True)
    start_date = fields.Datetime("Date de début de collecte", readonly=True)
    end_date = fields.Datetime("Date limite de collecte", readonly=True)
    state = fields.Many2one("study.questionnaire.response.state", string="État de la réponse")
    progress_status = fields.Many2one("study.questionnaire.response.progress.status", string="État d'avancement")    
    authored = fields.Datetime("Date de saisie des réponses", readonly=True)

    author = fields.Many2one("study.author", string="Platform d'étude", readonly=True)
    identifier_author = fields.Char("ID plateforme", readonly=True)
    redirect_url = fields.Char("Lien personnel de redirection vers le questionnaire", readonly=True)

    study_id = fields.Many2one("study.study", "Étude", readonly=True)
    study_questionnaire_id = fields.Many2one("study.questionnaire", string="Questionnaire", readonly=True)
    study_participant_id = fields.Many2one("study.participant", string="Participation", readonly=True)
    
    source = fields.Many2one("res.partner", string="Contact", domain=[("category_patient",'=',1)], readonly=True)
    firstname = fields.Char("Prénom", related="source.firstname")
    lastname = fields.Char("Nom", related="source.lastname")