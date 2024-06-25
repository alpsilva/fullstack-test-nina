import json
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

USERS_FILE_PATH = os.path.join(__location__, "mocked_users_data.json")
COMPLAINTS_FILE_PATH = os.path.join(__location__, "mocked_complaints_data.json")

# USERS_FILE_PATH = "./mocked_users_data.json"
# COMPLAINTS_FILE_PATH = "./mocked_complaints_data.json"

class Database:
    def __init__(self) -> None:
        self.users = []
        with open(USERS_FILE_PATH, 'r') as file:
            self.users = json.load(file)
        
        self.complaints = []
        with open(COMPLAINTS_FILE_PATH, 'r') as file:
            self.complaints = json.load(file)

    def insert_complaint(self):
        pass

    def get_complaints(self):
        return self.complaints

    def get_complaint(self, _id: str = None):
        result = list(filter(lambda x: x['id'] == _id, self.complaints))
        if len(result) > 0:
            return result[0]
        return None
    
    def update_complaint(self):
        pass

    def delete_complaint(self):
        pass

    def get_users(self):
        return self.users

    def get_user(self, _id: str = None):
        result = list(filter(lambda x: x['id'] == _id, self.users))
        if len(result) > 0:
            return result[0]
        return None
    
client = Database()