import json
from datetime import datetime
from typing import Dict

from mailbox_creator import MailboxCreator
from email_url_extractor import EmailUrlExtractor


class DatabaseCreator:
    def __init__(self, filepath: str) -> None:
        self.mailbox = MailboxCreator().create_mailbox(filepath)
        self.database = list()

        self._append_entry_to_database()
        self._sort_database(self.database)
        self._write_json_from_list(self.database)
    
    def _append_entry_to_database(self) -> None:
        count = 1
        for mail in self.mailbox:
            if url := EmailUrlExtractor().run_extraction(mail):
                self.database.append({"Count": count, "Date": mail["Date"], "Url": url[0], "Flag": "0"})
                count += 1

    def _sort_database(self, database: list[Dict]) -> None:
        database.sort(key=lambda x: datetime.strptime(x["Date"], "%a, %d %b %Y %H:%M:%S %z"))

    def _write_json_from_list(self, database: list[Dict]) -> None:
        json_object = json.dumps(database, indent=4)

        with open("database.json", "w") as outfile:
            outfile.write(json_object)
