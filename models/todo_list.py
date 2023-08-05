# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Todo(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = "todo.list"
    _description = 'Todo List App'

    name = fields.Char(string="Task", required=True)
    active = fields.Boolean(default=True)
    color = fields.Char()
    priority = fields.Char('Set Priority')
    date_time = fields.Datetime(string='Date',default=fields.Datetime.now)
    