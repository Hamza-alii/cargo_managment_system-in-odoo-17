# -*- coding: utf-8 -*-
{
    'name': 'Cargo Management',
    'version': '1.0',
    'category': 'Operations/Logistics',
    'summary': 'Manage cargo shipments, vehicles, and employees for efficient logistics.',
    'description': """
        This module helps in managing cargo shipments, vehicles, and employees 
        involved in the logistics process. It provides functionality for 
        tracking shipments, managing vehicle fleet, and keeping records of employees 
        working on the cargo operations.
    """,
    'author': 'Hamza',
    'website': 'http://www.yourwebsite.com',
    'depends': [
        'base', 
        'web', 
        'mail',  # Optional if you want to include email notification features
        'board',  # Required for dashboard views
    ],
    'data': [
        # Security files
        'security/ir.model.access.csv',
        'security/cargo_security.xml',

        # Views
        'views/cargo_shipment_views.xml',
        'views/cargo_vehicle_views.xml',
        'views/cargo_employee_views.xml',
        'views/cargo_dashboard.xml', 
        'views/cargo_menus.xml',

        # Reports
        'report/cargo_shipment_report.xml',
        'report/cargo_shipment_template.xml',

        # Data
        'data/cargo_sequence.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
