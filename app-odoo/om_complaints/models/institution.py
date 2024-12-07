from odoo import models, fields

class Institution(models.Model):
    _name = 'om_complaint.institution'
    _description = 'Institution'

    name = fields.Char(string='نام', required=True)
    ministry_id = fields.Many2one('om_complaint.ministry', string='وزارت خانه', required=True)
