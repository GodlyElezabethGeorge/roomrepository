# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'SupportHub Employees',
    'version': '1.0.0',
    'category': 'Employee Management',
    'author':'SupprotHub360',
    'sequence': -100,
    'summary': '',
    'description': '',
    'depends': ['mail'],
    'data': [
    'views/viewbar.xml',
    'views/supportview.xml',
    'views/female_employee.xml',
    'views/add_department_list.xml',
    'views/respartner.xml',
    'views/salaryinformation.xml',
    'security/ir.model.access.csv',
    ],
    'installable': True,
    'license': 'LGPL-3',
    'application':'True',
    'assets': {
        
    }
}