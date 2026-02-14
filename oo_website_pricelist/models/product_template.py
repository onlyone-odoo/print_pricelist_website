# Copyright 2025 Be OnlyOne
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    show_in_website_pricelist = fields.Boolean(
        string="Mostrar en lista web",
        default=True,
        help="Si está activo, el producto aparece en la página de listado de precios (/lista). "
        "Independiente de si está publicado en la tienda.",
    )

    @api.model
    def _cron_update_show_in_website_pricelist(self):
        """
        Scheduled action: set show_in_website_pricelist to True when any variant
        has stock (virtual_available > 0), False otherwise.
        Only considers saleable products; service type products are excluded
        (no stock concept, and some setups restrict writes on them).
        """
        templates = self.search([
            ("sale_ok", "=", True),
            ("type", "!=", "service"),
        ])
        with_stock = self.browse()
        without_stock = self.browse()
        for tmpl in templates:
            has_stock = any(
                getattr(v, "virtual_available", 0) > 0
                for v in tmpl.product_variant_ids
            )
            if has_stock:
                with_stock |= tmpl
            else:
                without_stock |= tmpl
        if with_stock:
            with_stock.write({"show_in_website_pricelist": True})
        if without_stock:
            without_stock.write({"show_in_website_pricelist": False})
