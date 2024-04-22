import mailbox
import email
from email import policy
import json
from re import search
from datetime import datetime
from typing import Union, Dict

from email_decoder import Base64Decoder, Iso88591Decoder

class DatabaseCreator:
    def __init__(self, filepath: str) -> None:
        self.mailbox = self.create_mailbox(filepath)
        self.database = list()
        self._append_entry_to_database()
        self.database.sort(key=lambda x: datetime.strptime(x["Date"], "%a, %d %b %Y %H:%M:%S %z"))
        self._write_json_from_list(self.database)

    def create_mailbox(self, path: str) -> mailbox.mbox:
        try:
            return mailbox.mbox(path, factory=self._factory_EmailMessage)
        except IsADirectoryError:
            exit("mbox is a directory")
    
    @staticmethod
    def _factory_EmailMessage(file):
        return email.message_from_binary_file(file, policy=policy.default)

    def _append_entry_to_database(self) -> None:
        count = 1
        for mail in self.mailbox:
            if "release" in mail["Subject"]:
                mail_body = mail.get_body(preferencelist=('html')).as_string()
                if url := self._extract_URL(mail_body):
                    self.database.append({"Count": count, "Date": mail["Date"], "Url": url, "Flag": "0"})
                    count += 1

    def _write_json_from_list(self, database: list[Dict]) -> None:
        json_object = json.dumps(database, indent=4)

        with open("database.json", "w") as outfile:
            outfile.write(json_object)

    def _extract_URL(self, mail: str) -> Union[str, None]:
        if "base64" in mail:
            mail = Base64Decoder.decode_email(mail)
        if "iso-8859-1" in mail:
            mail = Iso88591Decoder.decode_email(mail)
        
        if "just released" in mail:
            if match := search(r"<a href=\"(.+)\">", mail):
                return match.group(1)
