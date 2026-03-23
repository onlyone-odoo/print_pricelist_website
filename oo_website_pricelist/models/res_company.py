# Copyright 2025 Be OnlyOne
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import _, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    website_pricelist_primary_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Lista de precios principal (web)",
        help="Lista de precios que se muestra en la primera columna de precios en /lista.",
    )
    website_pricelist_secondary_id = fields.Many2one(
        comodel_name="product.pricelist",
        string="Lista de precios secundaria (web)",
        help="Si se configura, se muestra una columna adicional con esta lista. Dejar vacío para no mostrar.",
    )
    website_pricelist_show_shop_link = fields.Boolean(
        string="Mostrar columna «Ver en tienda»",
        default=True,
        help="Si está activo, en la página /lista se muestra la columna con el enlace al ecommerce por producto.",
    )
    website_pricelist_product_sort = fields.Selection(
        selection=[
            ("name", _("Nombre (A-Z)")),
            ("price", _("Precio (lista principal, menor a mayor)")),
        ],
        string=_("Orden de productos en /lista"),
        default="name",
        required=True,
        help=_(
            "Orden de las filas dentro de cada categoría web. "
            "En el sitio se puede usar ?sort=name o ?sort=price."
        ),
    )
