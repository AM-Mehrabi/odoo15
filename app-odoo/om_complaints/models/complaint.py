from odoo import models, fields

class Complaint(models.Model):
    _name = 'om_complaint.complaint'
    _description = 'Complaint'

    name = fields.Char(string='شکایت', related='complaint_id.name', store=True)
    description = fields.Text(string='توضیحات')
    ministry_id = fields.Many2one('om_complaint.ministry', string='وزارت خانه', required=True)
    institution_id = fields.Many2one('om_complaint.institution', string='نهاد', domain="[('ministry_id', '=', ministry_id)]", required = True)
    complaint_id = fields.Many2one('om_complaint.suggestion', string='شکایت', required=True)
    user_id = fields.Many2one('res.users', string='نام کاربر', default=lambda self: self.env.user)
    vote_count = fields.Integer(string='رای', default=0)
    
    def vote_up(self):
        for record in self:
            existing_vote = self.env['om_complaint.vote'].search([
                ('complaint_id', '=', record.id),
                ('user_id', '=', self.env.user.id)
            ], limit=1)

            if existing_vote:
                if existing_vote.vote_type == 'down':
                    existing_vote.write({'vote_type': 'up'})
                    record.vote_count += 1 
                return False

            self.env['om_complaint.vote'].create({
                'complaint_id': record.id,
                'user_id': self.env.user.id,
                'vote_type': 'up'
            })
            record.vote_count += 1  
            return True

    def vote_down(self):
        for record in self:
            existing_vote = self.env['om_complaint.vote'].search([
                ('complaint_id', '=', record.id),
                ('user_id', '=', self.env.user.id)
            ], limit=1)

            if existing_vote:
                if existing_vote.vote_type == 'up':
                    existing_vote.write({'vote_type': 'down'})
                    record.vote_count -= 1  
                return False

            self.env['om_complaint.vote'].create({
                'complaint_id': record.id,
                'user_id': self.env.user.id,
                'vote_type': 'down'
            })
            if record.vote_count > 0:
                record.vote_count -= 1  
            return True