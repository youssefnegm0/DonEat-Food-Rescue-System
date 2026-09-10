#2
import json
import os
from priority import PriorityManager

class DonationManager:

    def __init__(self):
        self.file_path = "donations.json"
        self.donations = self.load_donations()

    def load_donations(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return {}

    def save_donations(self):
        with open(self.file_path, "w") as file:
            json.dump(self.donations, file, indent=4)

    def generate_id(self):
         if len(self.donations) == 0:
            return "10001"
         ids = []
         for don_id in self.donations:
             ids.append(int(don_id))
         new_id = max(ids) + 1
         return str(new_id)

    def create_donation(self):
        print("\n--- Create New Donation ---")
        donor_name = input("Enter donor name: ")
        food_type = input("Enter food type: ")

        while True:
            quantity = input("Enter quantity: ")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            print("Error: quantity must be a number.")

        location = input("Enter location: ")

        expiry_date = input("Enter expiry date (YYYY-MM-DD): ")

        priority_engine = PriorityManager()
        priority_level = priority_engine.calculate_priority(expiry_date)

        donation_id = self.generate_id()

        new_donation = {
            "donation_id": donation_id,
            "donor_name": donor_name,
            "food_type": food_type,
            "quantity": quantity,
            "location": location,
            "expiry_date": expiry_date,
            "priority": priority_level,
            "status": "Pending"
        }

        self.donations[donation_id] = new_donation
        self.save_donations()

        print("Donation created successfully!")
        print("Your Donation ID is:", donation_id)

    def search_donation(self):
        print("\n--- Search Donation ---")
        search_id = input("Enter Donation ID to search: ")

        if search_id in self.donations:
            d = self.donations[search_id]
            print("\nDonation Found")
            print("ID: " , d['donation_id'])
            print("Donor: " , d['donor_name'])
            print("Food: " , d['food_type'])
            print("Quantity: " , d['quantity'])
            print("Location: " , d['location'])
            print("Expiry Date: ", d.get('expiry_date', 'N/A'))
            print("Status: " , d['status'])
        else:
            print("Donation not found.")