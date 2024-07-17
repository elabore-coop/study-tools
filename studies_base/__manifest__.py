# Copyright 2024 Clément Thomas ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "studies_base",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Clément Thomas",
    "license": "AGPL-3",
    "category": "",
    "summary": "Module containing base fields and views for studies",
    # any module necessary for this one to work correctly
    "depends": [
        "base",       
        "partner_firstname"       
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [        
        # "security/security.xml",        
        "data/studies_base_data.xml",       
        "security/ir.model.access.csv",       
        "views/study_config_views.xml",
        "views/study_study_views.xml",
        "views/study_menu.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}