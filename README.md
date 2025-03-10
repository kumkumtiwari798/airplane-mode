# Airplane Mode

## Overview

Airplane Mode is a Frappe Framework-based application that models a flight ticket system. This application implements various document types (DocTypes) and features related to airlines, airplanes, airports, passengers, ticket booking, and more. The app also includes a web portal for flight management and shop tracking at airports.

## Features

### Core Functionality

- **Airline Management**: Stores airline details like name, founding year, customer care number, and headquarters.
- **Airplane Management**: Tracks individual airplanes linked to airlines, storing model and seating capacity.
- **Airport Management**: Stores master data of airports with codes, city, and country details.
- **Passenger Management**: Maintains passenger records with names, date of birth, and unique ID.
- **Flight Ticket Booking**: Allows users to book tickets with source, destination, flight details, and status tracking.
- **Status Tracking**: Tickets progress through statuses like Booked, Checked-In, and Boarded with color-coded indicators.

### Advanced Features

- **Fetch From Mechanism**: Automatically fetches related field values from linked DocTypes.
- **Child Table for Add-Ons**: Passengers can purchase additional services like meals, seats, and extra baggage.
- **Auto Seat Assignment**: Assigns random seats to passengers upon ticket creation (e.g., 21A, 45C).
- **Flight Price Calculation**: Ticket prices include add-on costs and base flight prices.
- **Submission Restrictions**: A ticket cannot be submitted unless the status is Boarded.
- **Flight Scheduling**: Refactored to include an Airplane Flight DocType, tracking multiple flights for an airplane.
- **Connected Documents**: Enables easy navigation between linked airline, airplane, and ticket records.

### Web Features

- **Web View for Flights**:
  - `/flights`: Displays all flights.
  - `/flights/<flight_id>`: Shows flight details with a booking link.
- **Flight Booking Web Form**: Allows users to book tickets online.
- **Notification System**: Sends system notifications to managers 24 hours before flight departures.
- **Web-Based Seat Assignment**: Allows users to manually assign seats via a dialog box in the ticket form.

### Airport Shop Management Module

- **Shop Tracking**: Manages airport shops leased to third parties, storing tenant details, contract info, rent amounts, and expiration dates.
- **Rent Collection & Receipts**: Tracks rent payments and generates printable receipts.
- **Shop Availability**: Tracks occupied vs. available shops per airport.
- **Automated Rent Reminders**: Sends email reminders to tenants before due payments.
- **Web Portal for Shops**:
  - `/shops`: Lists all shops.
  - `/shops/<shop_id>`: Shows shop details with an interest form.

### Security & Access Control

- **Role-Based Permissions**:
  - **Airport Authority Personnel**: Full access to manage flights, shops, and tenants.
  - **Fleet Managers**: Manages airplanes and flight schedules.
  - **Travel Agents**: Books tickets and manages passengers they create.
  - **Flight Crew Members**: Can only view flight details and passenger lists.
- **Audit System**: New airplanes require an initial audit, only editable by Airport Authority Personnel.

### Reporting & Analytics

- **Airplanes by Airline Report**: Analyzes the number of airplanes per airline.
- **Add-On Popularity Report**: Shows the most frequently purchased add-ons.
- **Revenue by Airline Report**: Displays total revenue per airline with a donut chart.

## Installation

You can install this app using the Bench CLI:

```sh
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/kumkumtiwari798/airplane-mode.git --branch main
bench install-app airplane_mode
```
1. Clone the repository:
   ```sh
   git clone https://github.com/kumkumtiwari798/airplane-mode.git
   ```
2. Navigate to the project folder:
   ```sh
   cd airplane_mode
   ```
3. Install dependencies:
   ```sh
   bench get-app airplane_mode
   ```
4. Create a new site and install the app:
   ```sh
   bench new-site <site-name>
   bench --site <site-name> install-app airplane_mode
   ```
5. Start the development server:
   ```sh
   bench start
   ```
## Contributing
If you want to contribute:
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Added new feature"
   ```
4. Push to your forked repository:
   ```sh
   git push origin feature-name
   ```
5. Submit a **Pull Request**.

## License

This project is licensed under the MIT License.

## Contact
For any issues or inquiries, reach out via email: **kumkumtiwari23@navgurukul.org**.
