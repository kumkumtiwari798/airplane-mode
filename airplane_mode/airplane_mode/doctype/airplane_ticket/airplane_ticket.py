# Copyright (c) 2025, kumkum and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random


class AirplaneTicket(Document):
	def validate(self):	
	# Ensure no duplicate add-ons and calculate the total price
		total = self.flight_price
		if self.add_ons:
			unique_add_ons = set()
			valid_add_ons = []

			# Validate each add-on and calculate total price
			for add_on in self.add_ons:
				if add_on.item in unique_add_ons:
					frappe.msgprint(f"Duplicate add-on: {add_on.add_on_type}")
				else:
					unique_add_ons.add(add_on.item)
					valid_add_ons.append(add_on)
					total += add_on.amount
			
			# Set valid add-ons without duplicates
			self.add_ons = valid_add_ons
		# Set the total amount after add-ons
		self.total_amount = total
		self.validate_ticket_capacity()

	def before_submit(document):
		# Check if the status is not 'Boarded', throw an error befor doc submit
		if document.status != "Boarded":
			frappe.throw("This Airplane Ticket cannot be submitted because its status is not 'Boarded'.")

	# def before_insert(self):
	# 	number = random.randint(1, 20)
	# 	letter = random.choice(['A', 'B', 'C', 'D', 'E'])
	# 	self.seat = f"{number}{letter}"
		
	def get_seat(self):
		avlbl_seat = []
		letter = ['A', 'B', 'C', 'D', 'E']
		for num in range(1,51):
			for word in letter:
				seatn = f"{num}{word}"
				avlbl_seat.append(seatn)
		return avlbl_seat
	
	def before_insert(self):
		#for random seat selection when new ticket create
		random_seat = self.get_seat()
		self.seat = random.choice(random_seat)

		#randon gate selection when new ticket create
		random_integers = random.randint(1, 2)
		random_alphabets = random.choice(['A','B'])
		self.gate_number = f"{random_alphabets}{random_integers} Gate"
		

	def validate_ticket_capacity(self):
        # Fetch the  flight document
		flight_doc = frappe.get_doc("Airplane Flight", self.flight)

        # Fetch the airplane's capacity
		airplane_doc = frappe.get_doc("Airplane", flight_doc.airplane)
		capacity = airplane_doc.capacity

        # Count how many tickets have been issued for this flight
		issued_tickets = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})

        # If the number of issued tickets more then  the capacity, throw an error
		if issued_tickets >= capacity:
			frappe.throw(f"Cannot create a new ticket. The number of issued tickets ({issued_tickets}) exceeds the airplane's capacity ({capacity}).")
