# Copyright 2025
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    portal_pricelist_download = fields.Boolean(
        string="Allow portal pricelist download",
        default=False,
        help="If enabled, portal users can download their pricelist in XLSX from /my.",
    )
