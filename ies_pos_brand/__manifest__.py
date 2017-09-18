# -*- coding: utf-8 -*-
# Part of Inceptus ERP Solutions Pvt.ltd.
# See LICENSE file for copyright and licensing details.
{
    'name': "Inceptus POS Brand",

    'summary': """Branding for POS""",

    'description': """
        Branding for POS
    """,

    'author': "Inceptus.io",
    'website': "http://www.inceptus.io",

    'category': 'point of sale',
    'version': '1.1',

    'depends': ['point_of_sale'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

    'qweb': [
        'static/src/xml/pos_brand.xml',
    ],

}
