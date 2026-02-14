===========
Website Pricelist (Listado de precios)
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

This module adds a public website page that displays a table of products with their list price, effective price (according to the visitor's pricelist when logged in), stock and a link to the shop.

**Table of contents**

.. contents::
   :local:

Install
=======

This module depends on **website** and **sale**. Install the module from the Apps menu.

Configure
=========

No specific configuration is required. The page is available at `/lista` and a menu entry "Lista de precios" is added to the main website menu. You can move or hide it from Website → Configuration → Menus.

Usage
=====

1. Go to your website and open the "Lista de precios" menu (or go to `/lista`).
2. Use the search box to filter products by name.
3. When logged in, the "Precio efectivo" column shows the price according to the contact's pricelist; otherwise the list price is shown.
4. Use "Ver en tienda" to open the product in the shop.

Known issues / Roadmap
======================

* Adapted from a legacy website pricelist page (Odoo 13/15) for Odoo 17.

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
