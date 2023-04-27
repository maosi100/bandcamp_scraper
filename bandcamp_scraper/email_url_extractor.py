from typing import Union
from re import search
from base64 import b64decode
import mailbox


class EmailUrlExtractor:
    def run_extraction(self, mail: mailbox.mboxMessage) -> str:
        email_body = self.extract_emails(mail)
        return self.extract_urls(email_body)

    def extract_emails(self, mail: mailbox.mboxMessage) -> Union[str, None]:
        if "release" in mail["Subject"]:
            email_body = str(mail.get_body(preferencelist=('html')))

            if "base64" in email_body or "iso-8859" in email_body:
                email_body = self.decode_emails(email_body)

            return str(email_body)
    
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
