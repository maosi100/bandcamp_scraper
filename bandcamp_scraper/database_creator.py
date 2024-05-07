from re import search
from datetime import datetime
from typing import Optional, List, Dict

from json_writer import JSONWriter

class DatabaseCreator:
    def __init__(self) -> None:
        self.database = []

    def append_entries_to_database(self, extracted_mails: List[Dict]) -> None:
        for mail in extracted_mails:
            if url := self._extract_URL(mail["Body"]):
                self.database.append({"Count": 0, "Date": mail["Date"], "Url": url, "Flag": "0"})
        self.database.sort(key=lambda x: datetime.strptime(x["Date"], "%a, %d %b %Y %H:%M:%S %z"))
        self.add_counts()
        JSONWriter.write_from_list(self.database)

    @staticmethod
    def _extract_URL(mail: str) -> Optional[str]:
        if "just released" in mail:
            if match := search(r'<a href="([^"]+)">', mail):
                return match.group(1)

    def add_counts(self) -> None:
        for i, item in enumerate(self.database, 1):
            item["Count"] = i
