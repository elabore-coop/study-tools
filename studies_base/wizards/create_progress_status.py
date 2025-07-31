from datetime import datetime
from odoo import fields, models


class CreateProgressStatus(models.TransientModel):
    _name = "create.progress.status"
    _description = "create Progress Status"

    state = fields.Selection([
        ('DRAFT', 'Brouillon'),
        ('NOT-YET-RECRUITING', 'À venir'),
        ('RECRUITING', 'En cours de recrutement'),
        ('ACTIVE-BUT-NOT-RECRUITING', 'Active mais ne recrute plus'),
        ('COMPLETED', 'Terminée'),
        ('WITHDRAWN', 'Annulé')], string="Avancement de l'étude")


    def create_progress_status(self):
        study = self.env["study.study"].browse(self._context.get("active_ids"))
        study.progress_status_id.date_end = datetime.now()
        values = {
            "study_id": study.id,
            "state": self.state,
            "date_begin": datetime.now(),
            "date_end": None,
        }
        self.env["study.progress.status"].create(values)
        study.write({"updated": datetime.now()})
