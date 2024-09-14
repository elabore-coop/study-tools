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
    progress_status = fields.Many2one("study.participant.progress.status", string="Statut de la participation", readonly=True)
    state = fields.Many2one("study.participant.state", string="État de la participation", readonly=True)
        
    identifier = fields.Char("Idientifiants de l'enrôlement", readonly=True)

    created = fields.Datetime("Date de création")
    updated = fields.Datetime("Date mise à jour")

    
