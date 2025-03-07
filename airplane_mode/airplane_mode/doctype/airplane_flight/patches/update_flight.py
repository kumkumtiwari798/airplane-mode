import frappe

def execute():
    flights = frappe.get_all("Airplane Flight", filters={"docstatus": 1}, fields=["name", "route", "is_published"])

    for flight in flights:
        doc = frappe.get_doc("Airplane Flight", flight.name)
        doc.db_set("is_published", 1)  # Enable is_published
        if not doc.route:  
            doc.db_set("route", "Default Route")
