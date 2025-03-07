# Copyright (c) 2025, kumkum and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    # Fetch columns and data
    columns, data = get_columns(), get_data()

    # Prepare data for the chart
    chart = get_chart_data(data)

    # Generate report summary
    report_summary = get_report_summary(data)

    return columns, data, None , chart, report_summary

def get_columns():
    return [
        {"label": "Airport", "fieldname": "airport", "fieldtype": "Link", "options": "Airport Shop Details", "width": 300},
        {"label": "Total Shops", "fieldname": "total_shop", "fieldtype": "Int", "width": 200},
        {"label": "Occupied Shops", "fieldname": "occupied_shop", "fieldtype": "Int", "width": 200},
        {"label": "Available Shops", "fieldname": "available_shop", "fieldtype": "Int", "width": 200},
    ]

def get_data():
    # Fetch all airports and their shop counts
    airports = frappe.get_all(
        "Airport Shop Details", 
        fields=["airport", "total_shop", "occupied_shop", "available_shop"]
    )
    return airports

def get_chart_data(data):
    # Prepare labels and datasets for the donut chart
    labels = [row["airport"] for row in data]
    occupied_values = [row["occupied_shop"] for row in data]
    available_values = [row["available_shop"] for row in data]

    return {
        "data": {
            "labels": labels,
            "datasets": [
                {"name": "Occupied Shops", "values": occupied_values},
                {"name": "Available Shops", "values": available_values},
            ],
        },
        "type": "donut",  # Set chart type to donut
    }

def get_report_summary(data):
    # Calculate totals for summary
    total_shops = sum([row["total_shop"] for row in data])
    total_occupied = sum([row["occupied_shop"] for row in data])
    total_available = sum([row["available_shop"] for row in data])

    return [
        {"label": "Total Shops", "value": total_shops, "indicator": "Blue"},
        {"label": "Occupied Shops", "value": total_occupied, "indicator": "Red"},
        {"label": "Available Shops", "value": total_available, "indicator": "Green"},
    ]




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
