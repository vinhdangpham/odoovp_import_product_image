{
    'name': 'Import product images from Google Drive',
    'version': '17.0.1.0',
    'category': 'Inventory',
    'summary': 'Import images into product templates from Google Drive',
    'description': """
        This module allows importing images into product templates from Google Drive.
    """,
    'author': 'OdooVP',
    'support':'odoovp@gmail.com',
    'license': 'OPL-1',
    'website': '',
    'depends': ['stock'],
    'data': [
        'data/ir_config_parameter.xml',
        'security/ir.model.access.csv',
        'views/product_template.xml',
        'wizard/product_import_views.xml'
    ],
    'installable': True,
    'auto_install': False,
    'price': 29,
    'currency': 'USD',
    'external_dependencies': {
        'python': [
            'gdown',
        ],
    },
}
