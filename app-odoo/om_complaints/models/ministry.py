from odoo import models, fields

class Ministry(models.Model):
    _name = 'om_complaint.ministry'
    _description = 'Ministry'

    name = fields.Char(string='نام', required=True)
    institution_ids = fields.One2many('om_complaint.institution', 'ministry_id', string='نهادها')
