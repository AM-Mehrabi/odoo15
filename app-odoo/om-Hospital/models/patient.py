# -*- coding: utf-8 -*-
from datetime import date 
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string="Name", tracking=True, default='Odoo')
    ref = fields.Char(string="Refrence")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking='0', default='female')
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age', tracking='0')
    active = fields.Boolean(string="Active",default=True)
    # tax_report_line_ids = fields.Many2many(string="Tax Report Lines", comodel_name='account.tax.report.line', relation='account_tax_report_line_tags_rel', help="The tax report lines using this tag")
    # tax_negate = fields.Boolean(string="Negate Tax Balance", help="Check this box to negate the absolute value of the balance of the lines associated with this tag in tax report computation.")
    # country_id = fields.Many2one(string="Country", comodel_name='res.country', help="Country for which this tag is available, when applied on taxes.")
   
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0 
   