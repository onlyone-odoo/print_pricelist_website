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
        domain = [("sale_ok", "=", True)]
        if search:
            domain.append(("name", "ilike", search))

        ProductTemplate = request.env["product.template"].sudo()
        count = ProductTemplate.search_count(domain)
        total_pages = (count + limit - 1) // limit if count else 1
        page = max(1, min(int(page), total_pages))
        offset = (page - 1) * limit
        products = ProductTemplate.search(domain, limit=limit, offset=offset, order="name")

        partner = request.env.user.partner_id
        pricelist = partner.property_product_pricelist or request.env.company.pricelist_id
        if not pricelist:
            pricelist = request.env["product.pricelist"].sudo().search(
                [("currency_id", "=", request.env.company.currency_id.id)], limit=1
            )

        # Build rows with price and stock for template
        date = datetime.now().date()
        rows = []
        for prod in products:
            variant = prod.product_variant_id if prod.product_variant_count == 1 else (prod.product_variant_ids[:1] if prod.product_variant_ids else request.env["product.product"])
            if not variant:
                variant = request.env["product.product"]

            list_price = prod.list_price
            if pricelist and variant and variant.exists():
                try:
                    customer_price = pricelist._get_product_price(variant, 1.0, date=date)
                except Exception:
                    customer_price = list_price
            else:
                customer_price = list_price

            virtual_available = variant.virtual_available if variant else 0
            if virtual_available > 0:
                stock_label = _("In stock")
            elif variant and getattr(variant, "seller_ids", None):
                stock_label = _("On order")
            else:
                stock_label = _("Out of stock")

            currency = request.env.company.currency_id
            list_price_fmt = "%s %.2f" % (currency.symbol, list_price)
            customer_price_fmt = "%s %.2f" % (currency.symbol, customer_price)
            rows.append({
                "product": prod,
                "variant": variant,
                "list_price": list_price,
                "customer_price": customer_price,
                "list_price_fmt": list_price_fmt,
                "customer_price_fmt": customer_price_fmt,
                "stock_label": stock_label,
                "website_url": getattr(prod, "website_url", "/shop"),
            })

        return request.render(
            "oo_website_pricelist.webpage_pricelist",
            {
                "productos": products,
                "rows": rows,
                "search": search or "",
                "page": page,
                "total_pages": total_pages,
                "pricelist": pricelist,
                "partner": partner,
                "is_logged": not request.env.user._is_public(),
            },
        )
