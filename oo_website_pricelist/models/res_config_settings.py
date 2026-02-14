# Copyright 2025 Be OnlyOne
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    website_pricelist_primary_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Lista de precios principal (web)",
        related="company_id.website_pricelist_primary_id",
        readonly=False,
    )
    website_pricelist_secondary_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Lista de precios secundaria (web)",
        related="company_id.website_pricelist_secondary_id",
        readonly=False,
    )
