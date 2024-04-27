from re import search
from datetime import datetime
from typing import Union, List, Dict

from email_decoder import EmailDecoder
from mailbox_reader import MailboxReader
from json_writer import JSONWriter
    
class DatabaseCreator:
    def __init__(self, extracted_mails: List[Dict]) -> None:
        self.mailbox = extracted_mails
        self.database = []
        self.append_entry_to_database()
        self.database.sort(key=lambda x: datetime.strptime(x["Date"], "%a, %d %b %Y %H:%M:%S %z"))
        self.add_counts()
        JSONWriter.write_from_list(self.database)
    
    def append_entry_to_database(self) -> None:
        for mail in self.mailbox:
            if url := self._extract_URL(mail["Body"]):
                self.database.append({"Count": 0, "Date": mail["Date"], "Url": url, "Flag": "0"})

    @staticmethod
    def _extract_URL(mail: str) -> Union[str, None]:
        if "just released" in mail:
            if match := search(r'<a href="([^"]+)">', mail):
                return match.group(1)
        
    def add_counts(self) -> None:
        for i, item in enumerate(self.database, 1):
            item["Count"] = i


