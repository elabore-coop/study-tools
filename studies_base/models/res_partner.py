from odoo import fields, models, api
from odoo.addons.seintinelles_odoo_to_zato.models.webhook_model import WebhookModel
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model, WebhookModel):
    _inherit = "res.partner"
    _description="Contact"

    study_participant_ids = fields.One2many(
        comodel_name="study.participant",
        inverse_name="subject",
        string="Related study participations",
    )

    study_participant_count = fields.Integer(
        compute="_compute_study_participant_count", string="Study Participants count"
    )

    study_ids = fields.Many2many(
        comodel_name="study.study",
        string="Études liées au contact",
        compute="_compute_study_participant_count",
    )

    study_count = fields.Integer(
        compute="_compute_study_participant_count", string="Studies count"
    )

    def _compute_study_participant_count(self):
        for record in self:
            participant_ids = self.env["study.participant"].search(
                [("subject", "child_of", record.id)]
            )
            record.study_participant_count = len(participant_ids)
            record.study_ids = participant_ids.mapped('part_of').ids
            record.study_count = len(record.study_ids)

    def action_view_partner_study_participants(self):
        return {
            "name": self.name,
            "view_mode": "tree,form",
            "res_model": "study.participant",
            "type": "ir.actions.act_window",
            "domain": [("subject", "child_of", self.id)],
            "context": self.env.context,
        }

    def action_view_partner_study(self):
        return {
            "name": self.name,
            "view_mode": "tree,form",
            "res_model": "study.study",
            "type": "ir.actions.act_window",
            "context": self.env.context,
        }
