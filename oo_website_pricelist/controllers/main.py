# Copyright 2025 Be OnlyOne
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import datetime
from collections import defaultdict

from odoo import _, http
from odoo.http import request


class OoWebsitePricelist(http.Controller):
    """Controller for the public website pricelist table page."""

    @http.route("/lista", type="http", auth="public", website=True)
    def listado(self, page=1, search=None, **kw):
        """Render the product pricelist table grouped by web category.

        Only logged-in users see prices; public users see availability
        and a message to register to see prices.
        """
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
        products = ProductTemplate.search(
            domain, limit=limit, offset=offset, order="name"
        )

        company = request.env.company
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
        currency_primary = (
            pricelist_primary.currency_id if pricelist_primary else company.currency_id
        )
        currency_secondary = (
            pricelist_secondary.currency_id if pricelist_secondary else company.currency_id
        )

        is_logged = not request.env.user._is_public()
        # Group products by first public category (website_sale)
        category_groups = defaultdict(list)
        for prod in products:
            cat = None
            if getattr(prod, "public_categ_ids", None) and prod.public_categ_ids:
                cat = prod.public_categ_ids[0]
            category_groups[cat].append(prod)

        # Sort categories: named first (by name), then None as "Sin categoría web"
        sorted_cats = sorted(
            (c for c in category_groups if c is not None),
            key=lambda c: (c.sequence, c.name),
        )
        if None in category_groups:
            sorted_cats.append(None)

        groups = []
        for cat in sorted_cats:
            cat_products = category_groups[cat]
            cat_name = cat.name if cat else _("Sin categoría web")
            rows = []
            for prod in sorted(cat_products, key=lambda p: p.name):
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
                        return pricelist._get_product_price(
                            variant, 1.0, date=date
                        )
                    except Exception:
                        return default

                price_primary = _price(pricelist_primary)
                price_secondary = (
                    _price(pricelist_secondary) if show_secondary_column else None
                )

                row = {
                    "product": prod,
                    "variant": variant,
                    "primary_price": price_primary,
                    "primary_price_fmt": "%s %.2f"
                    % (currency_primary.symbol, price_primary),
                    "website_url": getattr(prod, "website_url", "/shop"),
                }
                if show_secondary_column:
                    row["secondary_price"] = price_secondary
                    row["secondary_price_fmt"] = "%s %.2f" % (
                        currency_secondary.symbol,
                        price_secondary,
                    )
                rows.append(row)

            groups.append({
                "category": cat,
                "category_name": cat_name,
                "rows": rows,
            })

        primary_header = _("Precio principal")
        if pricelist_primary and pricelist_primary.name:
            curr = pricelist_primary.currency_id
            primary_header = "%s (%s)" % (
                pricelist_primary.name,
                curr.name if curr else "",
            )
        secondary_header = ""
        if show_secondary_column and pricelist_secondary:
            curr = pricelist_secondary.currency_id
            secondary_header = "%s (%s)" % (
                pricelist_secondary.name,
                curr.name if curr else "",
            )

        return request.render(
            "oo_website_pricelist.webpage_pricelist",
            {
                "productos": products,
                "groups": groups,
                "search": search or "",
                "page": page,
                "total_pages": total_pages,
                "pricelist_primary": pricelist_primary,
                "pricelist_secondary": pricelist_secondary,
                "show_secondary_column": show_secondary_column,
                "primary_header": primary_header,
                "secondary_header": secondary_header,
                "partner": request.env.user.partner_id,
                "is_logged": is_logged,
                "message_register_to_see_prices": _(
                    "Registrarse para ver los precios"
                ),
            },
        )
