===========
Product Pricelist Direct Print (XLSX)
===========

.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

.. |badge3| image:: https://onlyone.odoo.com/web/image/website/1/logo/OnlyOne%20Soft?unique=dccda5b
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3


|badge1| |badge2| |badge3|

This module extends the functionality of Product Pricelist Direct Print to support export in XLSX format and to allow you to print or export price lists to Excel.

**Table of contents**

.. contents::
   :local:

Install
=======

This module depends on:

* **product_pricelist_direct_print** (OCA, product-attribute, 17.0)
* **report_xlsx** (OCA, reporting-engine, 17.0)

Install those addons first, then install this module.

Configure
=========

Go to Product > Configuration > Pricelists, or run the report from a pricelist / partner. Use the wizard "Print Pricelist" and choose "Export" (XLSX) when a single customer is selected.

Usage
=====

1. Go to a product pricelist or select partners.
2. Run the "Print Pricelist" action.
3. Configure filters and options, then click "Export" to download the XLSX.

Known issues / Roadmap
======================

* Adapted from OCA product_pricelist_direct_print_xlsx 18.0 to 17.0.

Bug Tracker
===========

* Help Contact

Credits
=======

Authors
~~~~~~~

* Be OnlyOne

Contributors
~~~~~~~~~~~~

* `Be OnlyOne. <https://onlyone.odoo.com/>`_
  * Matías Bressanello

Maintainers
~~~~~~~~~~~

This module is maintained by Be OnlyOne.
