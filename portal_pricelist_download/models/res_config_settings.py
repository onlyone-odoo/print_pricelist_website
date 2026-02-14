# Copyright 2025
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    portal_pricelist_download = fields.Boolean(
        string="Allow portal pricelist download",
        related="company_id.portal_pricelist_download",
        readonly=False,
    )
