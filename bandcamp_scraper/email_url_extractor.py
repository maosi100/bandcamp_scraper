from typing import Union
from re import search
import mailbox

from email_decoder import Base64Decoder, Iso88591Decoder


class EmailUrlExtractor:
    def run_extraction(self, mail: mailbox.mboxMessage) -> str:
        email_body = self.extract_emails(mail)
        return self.extract_urls(email_body)

    def extract_emails(self, mail: mailbox.mboxMessage) -> Union[str, None]:
        if "release" in mail["Subject"]:
            email_body = str(mail.get_body(preferencelist=('html')))

            if "base64" in email_body:
                email_body = Base64Decoder.decode_email(email_body)
            if "iso-8859-1" in email_body:
                email_body = Iso88591Decoder.decode_email(email_body)

            return str(email_body)
    
    @staticmethod
    def extract_urls(email_body):
        if "just released" in str(email_body):
            if match := search(r"<a href=\"(.+)\">", str(email_body)): 
                return match.groups(1)
            else:
                return False
