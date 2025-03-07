# import frappe

# def context(context):
#     context.shop = frappe.get_all(
#         "Shop Details",
#         filters={"status":"Available"},
#         fields={"shop_name","tenant_name","airport","rent_amount","area","start_date","expiry_date"}
#     )

import frappe

def get_context(context):
    # Fetch shops with status 'Available'
    context.available_shops = frappe.get_all(
        "Shop Details",
        filters={"status": "Available"},
        fields=["shop_name", "tenant_name", "rent_amount","expiry_date", "area", "airport"]
    )
    