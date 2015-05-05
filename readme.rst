=====================
inouk.recipe.odoo_cmd
=====================

inouk.recipe.odoo_cmd is an anybox.recipe.odoo console script that
adds the odoo.py command to a buildout Odoo server.

Installation
============

In the openerp section your buildout.cfg, add inouk.recipe.odoo_cmd egg:

::

    [openerp] 
    recipe = anybox.recipe.openerp:server
    ...

    # ask buildout to get the package
    eggs = inouk.recipe.odoo_cmd

    # ask the odoo recipe to create a script from inouk.recipe.odoo_cmd
    openerp_scripts = odoo_cmd=odoo.py  

Then buildout your server with *bin/buildout*.

Usage
=====

Once your buildout is finished, you can launch *bin/odoo.py*.

By typing bin/odoo.py you will be able to follow the Odoo developer tutorial and use the scaffold command.

Try bin/odoo.py scaffold

License
=======

inouk.recipe.odoo_cmd is licensed under the GNU Affero General Public License v3. See LICENCE.txt

