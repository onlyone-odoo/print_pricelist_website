# Copyright 2025 Be OnlyOne
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from odoo import _, http
from odoo.http import request


class OoWebsitePricelist(http.Controller):
    """Controller for the public website pricelist table page."""

    @http.route("/lista", type="http", auth="public", website=True)
    def listado(self, page=1, search=None, **kw):
        """Render the product pricelist table with search and pagination."""
        limit = 50
        offset = (int(page) - 1) * limit
        domain = [
            ("sale_ok", "=", True),
            ("show_in_website_pricelist", "=", True),
        ]
        if search:
            domain.append(("name", "ilike", search))

        ProductTemplate = request.env["product.template"].sudo()
        count = ProductTemplate.search_count(domain)
        total_pages = (count + limit - 1) // limit if count else 1
        page = max(1, min(int(page), total_pages))
        offset = (page - 1) * limit
        products = ProductTemplate.search(domain, limit=limit, offset=offset, order="name")

        company = request.env.company
        # Primary pricelist: from settings, or partner's, or first by currency
        pricelist_primary = company.website_pricelist_primary_id
        if not pricelist_primary:
            partner = request.env.user.partner_id
            pricelist_primary = (
                partner.property_product_pricelist
                or company.pricelist_id
                or request.env["product.pricelist"]
                .sudo()
                .search([("currency_id", "=", company.currency_id.id)], limit=1)
            )
        pricelist_secondary = company.website_pricelist_secondary_id
        show_secondary_column = bool(pricelist_secondary)

        date = datetime.now().date()
        currency = company.currency_id
        rows = []
        for prod in products:
            variant = (
                prod.product_variant_id
                if prod.product_variant_count == 1
                else (
                    prod.product_variant_ids[:1]
                    if prod.product_variant_ids
                    else request.env["product.product"]
                )
            )
            if not variant:
                variant = request.env["product.product"]

            list_price = prod.list_price

            def _price(pricelist, default=list_price):
                if not pricelist or not variant or not variant.exists():
                    return default
                try:
                    return pricelist._get_product_price(variant, 1.0, date=date)
                except Exception:
                    return default

            price_primary = _price(pricelist_primary)
            price_secondary = _price(pricelist_secondary) if show_secondary_column else None

            virtual_available = variant.virtual_available if variant else 0
            if virtual_available > 0:
                stock_label = _("In stock")
            elif variant and getattr(variant, "seller_ids", None):
                stock_label = _("On order")
            else:
                stock_label = _("Out of stock")

            row = {
                "product": prod,
                "variant": variant,
                "list_price": list_price,
                "list_price_fmt": "%s %.2f" % (currency.symbol, list_price),
                "primary_price": price_primary,
                "primary_price_fmt": "%s %.2f" % (currency.symbol, price_primary),
                "stock_label": stock_label,
                "website_url": getattr(prod, "website_url", "/shop"),
            }
            if show_secondary_column:
                row["secondary_price"] = price_secondary
                row["secondary_price_fmt"] = "%s %.2f" % (currency.symbol, price_secondary)
            rows.append(row)

        return request.render(
            "oo_website_pricelist.webpage_pricelist",
            {
                "productos": products,
                "rows": rows,
                "search": search or "",
                "page": page,
                "total_pages": total_pages,
                "pricelist_primary": pricelist_primary,
                "pricelist_secondary": pricelist_secondary,
                "show_secondary_column": show_secondary_column,
                "partner": request.env.user.partner_id,
                "is_logged": not request.env.user._is_public(),
            },
        )
