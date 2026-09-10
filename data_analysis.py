#5
import json
import os

class DataAnalyzer:
    def __init__(self, file_path="donations.json"):
        self.file_path = file_path
        self.donations = self.load_donations()

    def load_donations(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as file:
            data = json.load(file)
            return list(data.values())

    def total_donations(self):
        return len(self.donations)

    def total_food_rescued(self):
        total = 0
        for food in self.donations:
            if food.get("status") == "Completed":
                total += food.get("quantity", 0)
        return total

    def food_by_type(self):
        statistics = {}
        for food in self.donations:
            food_type = food.get("food_type", "Unknown")
            if food_type not in statistics:
                statistics[food_type] = 0
            statistics[food_type] += food.get("quantity", 0)
        return statistics

    def status_statistics(self):
        statistics = {}
        for food in self.donations:
            status = food.get("status", "Unknown")
            if status not in statistics:
                statistics[status] = 0
            statistics[status] += 1
        return statistics

    def priority_statistics(self):
        statistics = {"High": 0, "Medium": 0, "Low": 0}
        for food in self.donations:
            priority = food.get("priority", "Low")
            if priority in statistics:
                statistics[priority] += 1
        return statistics

    def largest_donation(self):
        if not self.donations:
            return None
        return max(self.donations, key=lambda food: food.get("quantity", 0))

    def generate_report(self):
        return {
            "total_donations": self.total_donations(),
            "total_food_rescued": self.total_food_rescued(),
            "food_by_type": self.food_by_type(),
            "status_statistics": self.status_statistics(),
            "priority_statistics": self.priority_statistics(),
            "largest_donation": self.largest_donation()
        }