import mailbox
from email import message
from typing import Optional, Dict

from email_decoder import EmailDecoder

class MailboxReader():
    def __init__(self) -> None:
        self.extracted_mails = []

    def extract_emails(self, mailbox : mailbox.mbox) -> Optional[list[Dict]]:
        self.extracted_mails = [
            self.extract_body(mail)
            for mail in mailbox if self.filter_mails(mail)
        ]
        return self.extracted_mails

    def extract_body(self, mail: message.EmailMessage) -> Optional[Dict]:
        return {
            "Date": mail["Date"],
            "Body": self._decode_mails(
                mail.get_body(preferencelist=('html')).as_string()
            )
        }

    @staticmethod
    def filter_mails(mail: message.EmailMessage) -> Optional[message.EmailMessage]:
        return mail if "release" in mail["Subject"] else None

    def _decode_mails(self, mail: str) -> str:
        return EmailDecoder(mail).decode()
