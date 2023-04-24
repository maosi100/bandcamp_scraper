from email_scraper import EmailScraper
import json
from sys import exit

class Database:

    def __init__(self, filepath=None):
        if filepath:
            self.create_database(filepath)

        self.database = self.open_database()
        self.length = self.database[-1]["Count"]

    def create_database(self, filepath: str):
        if self.validate_filepath(filepath):
            EmailScraper(filepath)

    @staticmethod
    def open_database():
        try:
            with open("./database.json", "r") as file:
                database_json = json.load(file)
                return database_json
        except FileNotFoundError:
            exit("Could not find database.json")

    @staticmethod
    def validate_filepath(filepath):
        if ".mbox" not in filepath:
            raise ValueError("Could not retrieve .mbox file")
        return True

    def get_release(self): 
        for item in self.database:
            if item["Flag"] == "0":
                item["Flag"] = "1"
                return item["Url"], item["Count"]

    def save_state(self):
        try:
            with open("./database.json", "w") as file:
                database = json.dumps(self.database, indent=4)
                file.write(database)
                return True
        except FileNotFoundError:
            print("Could not write database file")

    def set_back(self):
        for item in self.database:
            if item["Flag"] == "0":
                count = item["Count"] - 1
                self.database[(count - 1)]["Flag"] = "0"
                self.database[(count - 2)]["Flag"] = "0"
