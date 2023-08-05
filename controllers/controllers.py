# -*- coding: utf-8 -*-
# from odoo import http


# class OwlTodoApp(http.Controller):
#     @http.route('/owl_todo_app/owl_todo_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl_todo_app/owl_todo_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl_todo_app.listing', {
#             'root': '/owl_todo_app/owl_todo_app',
#             'objects': http.request.env['owl_todo_app.owl_todo_app'].search([]),
#         })

#     @http.route('/owl_todo_app/owl_todo_app/objects/<model("owl_todo_app.owl_todo_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl_todo_app.object', {
#             'object': obj
#         })
