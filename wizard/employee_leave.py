from odoo import api, fields, models


class LeaveWizard(models.TransientModel):
   
   
    _name = 'employee_leave.wizard'
    _description = 'Employee Leave Wizard'

    leave_reason = fields.Char(string='Leave Reason', required=True)