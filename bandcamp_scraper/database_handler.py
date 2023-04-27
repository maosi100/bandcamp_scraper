import json
from sys import exit
from typing import Dict, Union

from database_creator import DatabaseCreator

class Database:
    def __init__(self, filepath: str) -> None:
        if self._is_valid(filepath):
            DatabaseCreator(filepath)

        self.database = self.open_database()
        self.length = self.database[-1]["Count"]

    @staticmethod
    def open_database() -> Dict:
        try:
            with open("./database.json", "r") as file:
                database_json = json.load(file)
                return database_json
        except FileNotFoundError:
            exit("Could not find database.json")

    def save_state(self) -> bool:
        try:
            with open("./database.json", "w") as file:
                database = json.dumps(self.database, indent=4)
                file.write(database)
                return True
        except FileNotFoundError:
            print("Could not write database file")
            return False

    def get_release(self) -> Union[tuple[str, int], None]: 
        for item in self.database:
            if item["Flag"] == "0":
                item["Flag"] = "1"
                return item["Url"], item["Count"]

    def set_back(self) -> None:
        for item in self.database:
            if item["Flag"] == "0":
                count = item["Count"] - 1
                self.database[(count - 1)]["Flag"] = "0"
                self.database[(count - 2)]["Flag"] = "0"

    @staticmethod
    def _is_valid(filepath) -> bool:
        if ".mbox" not in filepath:
            raise ValueError("Could not retrieve .mbox file")
        return True
