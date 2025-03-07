# Copyright (c) 2025, kumkum and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ShopDetails(Document):
	def validate(self):
		if not self.rent_amount:  # Agar rent amount empty hai
            # Rent Setting ko fetch karo
			rent_setting = frappe.get_single('Rent Settings')  
			# Rent Setting se rent amount ko default value set karo
			self.rent_amount = rent_setting.rent_amount  

