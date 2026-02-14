===========
Portal Pricelist Download
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

This module extends the functionality of the customer portal to support downloading the contact's pricelist in XLSX format and to allow portal users to get their price list from "My Account".

**Table of contents**

.. contents::
   :local:

Install
=======

This module depends on:

* **portal** (Odoo core)
* **product_pricelist_direct_print_xlsx** (this repository, 17.0)

Install those addons first, then install this module.

Configure
=========

Go to Settings > Portal Pricelist (or General) and enable "Allow portal pricelist download". Ensure portal contacts have a pricelist set (Sales & Purchase > Pricelist on the partner).

Usage
=====

1. Log in as a portal user.
2. Go to My Account (/my).
3. Use the "Price List (XLSX)" link to download the pricelist as Excel.

Known issues / Roadmap
======================

* None at this time.

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
