#4
import json
import os

class recipient_manager:

    def __init__(self):
        self.requests = self.load_requests()

    def load_requests(self):
        if os.path.exists("requests.json"):
            with open("requests.json", "r") as file:
                return json.load(file)
        return {}

    def save_requests(self):
        with open("requests.json", "w") as file:
            json.dump(self.requests, file, indent=4)

    def request_donation(self, request_id, donation_id, recipient_id):
        req_id_str = str(request_id)

        if req_id_str in self.requests:
            return False

        request = {
            "request_id": req_id_str,
            "donation_id": donation_id,
            "recipient_id": recipient_id,
            "status": "Pending"
        }

        self.requests[req_id_str] = request
        self.save_requests()

        return True

    # change status

    def advance_status(self, request_id):

        req_id_str = str(request_id)

        if req_id_str not in self.requests:
            return False

        status = self.requests[req_id_str]["status"]

        if status == "Pending":
            self.requests[req_id_str]["status"] = "Accepted"
        elif status == "Accepted":
            self.requests[req_id_str]["status"] = "Collected"
        elif status == "Collected":
            self.requests[req_id_str]["status"] = "Completed"

        else:
            return False

        self.save_requests()

        return True