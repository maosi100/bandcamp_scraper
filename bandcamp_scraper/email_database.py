import json
from datetime import datetime


class EmailDatabase:
    def __init__(self, extracted_emails):
        self.database = extracted_emails

    def sort_database(self):
        self.database.sort(key=lambda x: datetime.strptime(x["Date"], "%a, %d %b %Y %H:%M:%S %z"))

    def write_json_from_list(self):
        json_object = json.dumps(self.database, indent=4)

        with open("database.json", "w") as outfile:
            outfile.write(json_object)
