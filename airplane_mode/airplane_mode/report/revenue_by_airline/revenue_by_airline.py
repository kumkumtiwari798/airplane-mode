# Copyright (c) 2025, kumkum and contributors
# For license information, please see license.txt


import frappe
from frappe.utils import flt  #floating point number 

def execute(filters=None):
    columns, data = get_columns(), get_data()
    total_revenue = sum([row['revenue'] for row in data])
    
    chart = get_chart_data(data)
    report_summary = get_report_summary(total_revenue)

    return columns, data, None, chart, report_summary

def get_columns():
    return [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 300},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 300}
    ]

def get_data():
    airlines = frappe.get_all("Airline", fields=["name"])
    data = []
    for airline in airlines:
        revenue = frappe.db.sql("""
            SELECT SUM(at.total_amount)
            FROM `tabAirplane Ticket` at
            JOIN `tabAirplane Flight` af ON at.flight = af.name
            JOIN `tabAirplane` a ON af.airplane = a.name
            WHERE a.airline = %s
        """, (airline.name,))
        
        revenue = revenue[0][0] if revenue and revenue[0][0] is not None else 0
        data.append({
            "airline": airline.name,
            "revenue": flt(revenue)
        })
    return data

def get_chart_data(data):
    labels = [row["airline"] for row in data]
    values = [row["revenue"] for row in data]
    return {
        "data": {
            "labels": labels,
            "datasets": [{"name": "Revenue", "values": values}]
        },
        "type": "donut"
    }

def get_report_summary(total_revenue):
    return [
        {"label": "Total Revenue", "value": frappe.utils.fmt_money(total_revenue), "indicator": "Green"}
    ]





# import frappe
# from frappe import _


# def execute(filters: dict | None = None):
# 	"""Return columns and data for the report.

# 	This is the main entry point for the report. It accepts the filters as a
# 	dictionary and should return columns and data. It is called by the framework
# 	every time the report is refreshed or a filter is updated.
# 	"""
# 	columns = get_columns()
# 	data = get_data()

# 	return columns, data


# def get_columns() -> list[dict]:
# 	"""Return columns for the report.

# 	One field definition per column, just like a DocType field definition.
# 	"""
# 	return [
# 		{
# 			"label": _("Column 1"),
# 			"fieldname": "column_1",
# 			"fieldtype": "Data",
# 		},
# 		{
# 			"label": _("Column 2"),
# 			"fieldname": "column_2",
# 			"fieldtype": "Int",
# 		},
# 	]


# def get_data() -> list[list]:
# 	"""Return data for the report.

# 	The report data is a list of rows, with each row being a list of cell values.
# 	"""
# 	return [
# 		["Row 1", 1],
# 		["Row 2", 2],
# 	]
