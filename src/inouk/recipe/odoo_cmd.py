# coding: utf-8
"""
odoo.py command for Odoo servers built using anybox.recipe.odoo
"""
__version__ = '0.2.0'

try:
    from odoo import main
except:
    from odoo.cli.command import main


def buildout_entry_point():
    main()
