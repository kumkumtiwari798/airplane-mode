import frappe

def execute():
    flights = frappe.get_all("Airplane Flight", filters={"docstatus": 1}, fields=["name", "route"])

    for flight in flights:
        dynamic_route = f"flights/{flight.name}" 
        frappe.db.set_value("Airplane Flight", flight.name, "route", dynamic_route)
