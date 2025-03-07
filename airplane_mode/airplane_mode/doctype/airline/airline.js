// Copyright (c) 2025, kumkum and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
        if (frm.doc.website) {
            // Add a web link using frm.add_web_link(url, lable) mathod
            frm.add_web_link(frm.doc.website, 'Visit Website'); // This will create a clickable link
        }
    }
});
