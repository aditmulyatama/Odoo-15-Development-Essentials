{
    "name": "Library Book Checkout",
    "description": "Members can borrow books from the library.",
    "author": "Daniel Reis",
    "depends": ["library_member", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/library_menu.xml",
        "views/checkout_view.xml",
        "wizard/checkout_mass_message_wizard_view.xml",
        "data/stage_data.xml",
    ],
}