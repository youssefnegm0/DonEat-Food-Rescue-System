#  DonEat - Smart Food Rescue System

**DonEat** is a Python-based Object-Oriented console application designed to bridge the gap between food donors and those in need. It manages the entire lifecycle of a food donation, utilizing a Smart Priority algorithm to ensure food is rescued before it expires.

##  Features
- **User Authentication:** Secure login and registration system with role-based routing (Donor, Receiver, Volunteer).
- **Smart Priority Engine:** Automatically calculates donation urgency (Urgent, High, Medium, Low) based on expiry dates.
- **Data Persistence:** All transactions and user data are securely stored using fast JSON dictionary structures.
- **Robust Validation:** Extensive Exception Handling (`try-except`) to prevent system crashes from invalid user inputs.
- **Analytics Dashboard:** Generates real-time reports on total food rescued and donation statistics.

##  Project Structure (Modules)
The system is built using clean OOP principles, separated into independent modules:
- `main.py`: The entry point and main dashboard logic.
- `auth.py`: Handles user registration, ID generation, and validation.
- `donation_manager.py`: Manages the logging and searching of food donations.
- `priority.py`: The time-engine that calculates days left until expiry.
- `recipient_manager.py`: Tracks request statuses (Pending -> Completed).
- `data_analysis.py`: Parses JSON data to generate system-wide statistics.

##  How to Run
1. Ensure you have Python installed on your system.
2. Install the required data visualization library:
   ```bash
   pip install matplotlib
```bash
python gui_main.py
