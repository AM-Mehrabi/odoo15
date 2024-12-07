from odoo import fields, models

class ComplaintVote(models.Model):
    _name = 'om_complaint.vote'
    _description = 'Complaint Vote'

    complaint_id = fields.Many2one('om_complaint.complaint', string='شکایت', required=True)
    user_id = fields.Many2one('res.users', string='نام کاربر', required=True)
    vote_type = fields.Selection([('up', 'مثبت'), ('down', 'منفی')], string='نوع رای', required=True)

    _sql_constraints = [
        ('unique_user_complaint', 'unique(complaint_id, user_id)', 'هر کاربر تنها یک بار می‌تواند برای هر شکایت رای دهد.')
    ]
