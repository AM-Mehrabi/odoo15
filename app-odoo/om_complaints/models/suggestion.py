from odoo import models, fields

class Suggestion(models.Model):
    _name = 'om_complaint.suggestion'
    _description = 'Suggestion'

    name = fields.Char(string='نام')
    ministry_id = fields.Many2one('om_complaint.ministry', string='وزارت خانه', required=True)
