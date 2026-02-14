# Copyright 2025
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import io

import xlsxwriter

from odoo import http
from odoo.http import request

from odoo.addons.portal.controllers.portal import CustomerPortal


class CustomerPortalPricelist(CustomerPortal):
    """Extend portal to pass pricelist download flag to template."""

    def _prepare_portal_layout_values(self):
        values = super()._prepare_portal_layout_values()
        company = request.env.company
        partner = request.env.user.partner_id
        values["company"] = company
        values["show_pricelist_download"] = bool(
            company.portal_pricelist_download and partner.property_product_pricelist
        )
        return values


class PortalPricelistDownload(http.Controller):
    """Controller to allow portal users to download their pricelist as XLSX."""

    @http.route(
        "/my/pricelist/download",
        type="http",
        auth="user",
        methods=["GET"],
        website=True,
    )
    def pricelist_download(self, **kw):
        """Generate and return the portal user's pricelist as XLSX."""
        if not request.env.user._is_portal():
            return request.redirect("/my")
        if not request.env.company.portal_pricelist_download:
            return request.redirect("/my")
        partner = request.env.user.partner_id
        pricelist = partner.property_product_pricelist
        if not pricelist:
            return request.redirect("/my")
        Wizard = request.env["product.pricelist.print"].sudo()
        wizard = Wizard.create(
            {
                "partner_ids": [(6, 0, [partner.id])],
                "pricelist_id": pricelist.id,
            }
        )
        report_model = request.env[
            "report.product_pricelist_direct_print_xlsx.report"
        ].sudo()
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {"in_memory": True})
        report_model.generate_xlsx_report(workbook, {}, wizard)
        workbook.close()
        output.seek(0)
        filename = "pricelist_%s.xlsx" % (pricelist.name or "pricelist",)
        filename = filename.replace(" ", "_")
        return request.make_response(
            output.getvalue(),
            headers=[
                (
                    "Content-Type",
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                ),
                ("Content-Disposition", 'attachment; filename="%s"' % filename),
            ],
        )
