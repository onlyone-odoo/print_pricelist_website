# Copyright 2025
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Portal Pricelist Download",
    "summary": "Allow portal users to download their pricelist in XLSX format",
    "version": "17.0.1.0.0",
    "category": "Portal",
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "portal",
        "product_pricelist_direct_print_xlsx",
    ],
    "data": [
        "views/res_config_settings_views.xml",
        "views/portal_templates.xml",
    ],
}
