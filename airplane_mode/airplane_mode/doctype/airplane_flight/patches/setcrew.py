# import frappe

# def execute():
#     flights = frappe.get_all(
#         "Airplane Flight",
#         filters={"docstatus":1},
#         fields=["name","crew_members",])
#     crew_members = frappe.get_all("Crew Members", fields=["crew_member_name", "role"])
    
#     for flight in flights.crew_members:

#     # frappe.db.commit()    
        