# -*- coding: utf-8 -*-
{
    'name': "miipl_wkf",

    'summary': """
        Implementation for the approval work flow for MIIPL sales order.
        """,

    'description': """
        This module adds workflows and transitions for approval of sales order and quotation within MIIPL
    """,

    'author': "Optibiz India",
    'website': "http://www.optibiz.in",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'miipl_msp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'workflows/flows.xml',
        'views/sale_order_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
