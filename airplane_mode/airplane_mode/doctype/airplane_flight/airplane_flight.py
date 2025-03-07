# Copyright (c) 2025, kumkum and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
import random


class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.db_set("status","Completed")
	def before_save(self):
        # Calculate the total crew members from the child table
		if self.crew_members:  # Check if child table has data
			total_crew = len(self.crew_members)  # Count the number of entries in the child table
			self.total_crew_members = total_crew  # Update the read-only field in the parent doctype
		else:
			self.total_crew_members = 0  # Default to 0 if no crew members        



	