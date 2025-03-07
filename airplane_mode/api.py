import frappe

def update_shop_counts(doc, method):
    # Get the airport linked to the shop
    airport_name = doc.airport

    # Calculate total and occupied shops
    total_shop = frappe.db.count('Shop Details', filters={'airport': airport_name})
    occupied_shop = frappe.db.count('Shop Details', filters={'airport': airport_name, 'status': 'Occupied'})
    available_shop = frappe.db.count('Shop Details', filters={'airport': airport_name, 'status': 'Available'})

    # Update the total and occupied shop counts in the Airports doctype
    frappe.db.set_value('Airport Shop Details', airport_name, 'total_shop', total_shop)
    frappe.db.set_value('Airport Shop Details', airport_name, 'occupied_shop', occupied_shop)
    frappe.db.set_value('Airport Shop Details', airport_name, 'available_shop',available_shop)
