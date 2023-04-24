from re import search
from base64 import b64decode
import json
from datetime import datetime
from mailbox_creator import Mailbox


class EmailScraper:
    def __init__(self, filepath) -> None:
        self.mailbox = Mailbox(filepath)
        self.database = list()
        self.email_extractor()
        self.sort_database()
        self.add_increment()
        self.write_json_from_list()

    def add_increment(self):
        for i, item in enumerate(self.database, 1):
            item["Count"] = i
        return True

    def email_extractor(self):
        for mail in self.mailbox.mailbox:
            if "release" in mail["Subject"]:
                email_body = str(mail.get_body(preferencelist=('html')))

                if "base64" in email_body or "iso-8859" in email_body:
                    email_body = self.email_decoder(email_body)

                if url := self.html_extractor(email_body):
                    self.database.append({"Count": 1, "Date": mail["Date"], "Url": url[0], "Flag": "0"})
    
    @staticmethod
    def email_decoder(email_body):
        if "base64" in email_body:
            stripped_body = search("^.+base64(.+)$", str(email_body).replace("\n", ""))
            return b64decode(stripped_body.groups(1)[0]).decode('utf-8')

        if "iso-8859-1" in email_body:
            stripped_body = search("^.+iso-8859-1(.+)$", str(email_body).replace("\n", ""))
            return str(stripped_body.groups(1)[0]).encode("utf-8")

    def html_extractor(self, email_body):
        if "just released" in str(email_body):
            if match := search(r"<a href=\"(.+)\">", str(email_body)) or search(r"<a href=3D\"(.+)\">", str(email_body)):
                return match.groups(1)
            else:
                return False

    def sort_database(self):
        self.database.sort(key=lambda x: datetime.strptime(x["Date"], "%a, %d %b %Y %H:%M:%S %z"))

    def write_json_from_list(self):
        json_object = json.dumps(self.database, indent=4)

        with open("database.json", "w") as outfile:
            outfile.write(json_object)
