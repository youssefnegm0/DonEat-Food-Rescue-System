#3
from datetime import datetime

class PriorityManager:
    
    def calculate_priority(self, expiry_date_str):
        try:
            expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d").date()
            today = datetime.now().date()
            
            days_left = (expiry_date - today).days

            if days_left < 0:
                return "Expired"
            elif days_left <= 1:
                return "Urgent"
            elif days_left <= 3:
                return "High"
            elif days_left <= 7:
                return "Medium"
            else:
                return "Low"
                
        except ValueError:
            return "Unknown"