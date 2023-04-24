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
                input = mail.get_body(preferencelist=('html'))
                input = self.email_encoder(input)
                if url := self.html_extractor(input):
                    self.database.append({"Count": 1, "Date": mail["Date"], "Url": url[0], "Flag": "0"})
    
    def email_encoder(self, input):
        if "base64" in str(input):
            input_stripped = search("^.+base64(.+)$", str(input).replace("\n", "")) 
            input = b64decode(input_stripped.groups(1)[0]).decode('utf-8')

        if "iso-8859-1" in str(input):
            input_stripped = search("^.+iso-8859-1(.+)$", str(input).replace("\n", ""))
            input = str(input_stripped.groups(1)[0]).encode("utf-8")
        
        return input

    def html_extractor(self, input):
        if "just released" in str(input):
            if match := search(r"<a href=\"(.+)\">", str(input)) or search(r"<a href=3D\"(.+)\">", str(input)):
                return match.groups(1)
            else:
                return False

    def sort_database(self):
        self.database.sort(key=lambda x: datetime.strptime(x["Date"], "%a, %d %b %Y %H:%M:%S %z"))

    def write_json_from_list(self):
        json_object = json.dumps(self.database, indent=4)

        with open("database.json", "w") as outfile:
            outfile.write(json_object)
