from datetime import datetime
from odoo import api,fields,models

class Supporthub_Employees(models.Model):
    _name = "supporthub.employees"
    _description = "Supporthub Employees"
    _inherit = ["mail.thread","mail.activity.mixin"]

    
   

    name = fields.Char(string='Employee Name', tracking=True)
    age = fields.Integer(string='Employee Age')
    gender = fields.Selection([('male','male'),('female','female'),('others','others')],string='Employee Gender')
    active = fields.Boolean(string="Active",default=True)
    user_id = fields.Many2one('res.users',string='User Id')
    activity_ids = fields.One2many('mail.activity', 'calendar_event_id', string='Activities')
    department_name = fields.Many2one('supporthub.department',string='Select Department')
    emp_products = fields.One2many('employee.products', 'productid', string='Products')
    ref = fields.Char(string='Reference')
    state = fields.Selection([('draft','Draft'),('in_consultation','In Consultation'),('done','Done'),('cancel','Cancelled')],string="Status")

  

class Add_Deparment(models.Model):
    _name = "supporthub.department"
    _descripton = "Employee Department"
  

    name = fields.Char(string='Department Name')    
    datetime = fields.Datetime(string='Date')
    date = fields.Date(string='Time')



    




class EmployeeProducts(models.Model):
    _name = 'employee.products'
    _description = 'Employee Products'
    productid = fields.Many2one(string='Product',comodel_name='supporthub.employees',help="")
    ref = fields.Char(string="Reference")
    description=fields.Text(string="Description")
    quantity=fields.Float('Quantity')
    price = fields.Float('Price')



    @api.onchange('productid')

    def onchange_productid(self):
        self.ref=self.productid.ref



class ResPartner(models.Model):
    _inherit = 'res.partner'
    landmark=fields.Char(string="Landmark")



class SalaryInformation(models.Model):
   _inherit = 'hr.employee'    
   salary=fields.Char(string="Enter Salary")




