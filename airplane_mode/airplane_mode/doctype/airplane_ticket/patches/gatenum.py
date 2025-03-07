import frappe
import random
def execute():
    tickets = frappe.get_all(
        "Airplane Ticket",
        fields=["name", "status", "gate_number"])
    random_ga = random.randint(1,2)
    random_te = random.choice(['A','B'])
    random_gate = f"{random_ga}{random_te} Gate"
    for ticket in tickets:
        if not ticket.get("gate_number"):  # Only update if gate_number is not set
            random_ga = random.randint(1, 2)
            random_te = random.choice(['A', 'B'])
            random_gate = f"{random_ga}{random_te} Gate"
            
            # Update the gate_number field
            frappe.db.set_value("Airplane Ticket", ticket["name"], "gate_number", random_gate)


        # frappe.db.set_value("gate_number",random_gate)

    frappe.db.commit()
