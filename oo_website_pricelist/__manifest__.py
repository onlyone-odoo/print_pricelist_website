# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Website Pricelist (Listado de precios)",
    "summary": "Página web con tabla de productos y precios según la lista del visitante",
    "version": "17.0.1.0.0",
    "category": "Website",
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
    "depends": ["website", "sale", "website_sale"],
    "data": [
        "data/cron_data.xml",
        "views/res_config_settings_views.xml",
        "views/product_views.xml",
        "views/views.xml",
        "views/templates.xml",
    ],
}
