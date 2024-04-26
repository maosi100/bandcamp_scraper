import json
from typing import Dict

class JSONWriter():
    @staticmethod
    def write_from_list(database: list[Dict]) -> None:
        json_object = json.dumps(database, indent=4)

        with open("database.json", "w") as outfile:
            outfile.write(json_object)
