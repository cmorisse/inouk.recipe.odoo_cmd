# coding: utf-8
"""
odoo.py command for Odoo servers built using anybox.recipe.odoo
"""
__version__ = '0.1.0'
from odoo import main


def buildout_entry_point():
    main()
