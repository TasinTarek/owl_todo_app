# -*- coding: utf-8 -*-
{
    'name': "Smart TODO",

    'summary': """Smart To-Do List App""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Tasin Tarek",
    'website': "https://www.tasintarek-odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/todo_list_view.xml',
        # Menus
        'menus/menu.xml'
    ],
    'assets': {
        'web.assets_backend': [
            '/owl_todo_app/static/src/components/todo_list/todo_list.js',
            '/owl_todo_app/static/src/components/todo_list/todo_list.xml',
            '/owl_todo_app/static/src/components/todo_list/todo_list.scss',
            '/owl_todo_app/static/src/components/todo_list/todo_list.css',
        ],
        'web.assets_frontend': [
        ],
        'web.assets_common': [
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
