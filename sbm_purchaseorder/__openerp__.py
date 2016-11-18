{
    "name": "Purchase Order",
    "version": "1.0",
    "depends": [
                "base",
                "purchase",
                "hr",
                "product",
                "sbm_purchase",
                "sbm_inherit"
                ],
    "author": "Suprabakti Mandiri",
    "category": "Purchase Suprabakti",
    "description": """Modul ini digunakan untuk Menggolah Data Purchase Order""",
    "init_xml": [],
    'update_xml': ["view_purchaseorder.xml","setting.xml","menu.xml"],
    'demo_xml': [],
    'installable': True,
    'active': False,
    'certificate': '',
    'js':['static/src/js/purchaseorder.js'],
}