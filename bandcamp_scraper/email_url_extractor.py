from re import search
from base64 import b64decode
import mailbox


class EmailUrlExtractor:
    def __init__(self, mailbox: mailbox.mbox) -> None:
        self.mailbox = mailbox
        self.database = list()

    def extract_emails(self):
        count = 1
        for mail in self.mailbox:
            if "release" in mail["Subject"]:
                email_body = str(mail.get_body(preferencelist=('html')))

                if "base64" in email_body or "iso-8859" in email_body:
                    email_body = self.decode_emails(email_body)

                if url := self.extract_urls(email_body):
                    self.database.append({"Count": count, "Date": mail["Date"], "Url": url[0], "Flag": "0"})
                    count += 1
    
    @staticmethod
    def decode_emails(email_body):
        if "base64" in email_body:
            stripped_body = search("^.+base64(.+)$", email_body.replace("\n", ""))
            return b64decode(stripped_body.groups(1)[0]).decode('utf-8')

        if "iso-8859-1" in email_body:
            replaced_body = email_body.replace("\n", "").replace("3D", "")
            stripped_body = search("^.+iso-8859-1(.+)$", replaced_body)
            return str(stripped_body.groups(1)[0]).encode("utf-8")
    
    @staticmethod
    def extract_urls(email_body):
        if "just released" in str(email_body):
            if match := search(r"<a href=\"(.+)\">", str(email_body)): 
                return match.groups(1)
            else:
                return False
