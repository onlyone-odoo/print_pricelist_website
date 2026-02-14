# Copyright 2025 Be OnlyOne
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    show_in_website_pricelist = fields.Boolean(
        string="Mostrar en lista web",
        default=True,
        help="Si está activo, el producto aparece en la página de listado de precios (/lista). "
        "Independiente de si está publicado en la tienda.",
    )
