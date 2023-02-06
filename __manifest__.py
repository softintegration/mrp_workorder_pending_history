# -*- coding: utf-8 -*- 


{
 'name': 'Manufacturing Work Order pending history',
 'author': 'Soft-integration',
 'application': False,
 'installable': True,
 'auto_install': False,
 'qweb': [],
 'description': False,
 'images': [],
 'version': '1.0.1',
 'category': 'Manufacturing/Manufacturing',
 'demo': [],
 'depends': ['mrp'],
 'data': [
     'security/ir.model.access.csv',
     'views/mrp_workorder_views.xml',
     'wizard/mrp_workorder_pending_confirmation_views.xml'
    ],
 'license': 'LGPL-3',
 }