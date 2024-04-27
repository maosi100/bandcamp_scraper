import mailbox
import email
from email import policy
from email import message
from typing import Optional, Dict

from email_decoder import EmailDecoder

class MailboxReader():
    def __init__(self, filepath: str) -> None:
        self.mailbox = self.connect_mailbox(filepath)
        self.extracted_mails = []
        self.extract_emails()

    def connect_mailbox(self, filepath: str) -> Optional[mailbox.mbox]:
        if not filepath.endswith('mbox'):
            raise ValueError(f"{filepath} is not an mbox file")
        try:
            return mailbox.mbox(filepath, factory=self._factory_EmailMessage)
        except IsADirectoryError:
            raise IsADirectoryError(f"{filepath} is a directory")

    @staticmethod
    def _factory_EmailMessage(file):
        return email.message_from_binary_file(file, policy=policy.default)

    def extract_emails(self) -> None:
        self.extracted_mails = [
            self.extract_body(mail)
            for mail in self.mailbox if self.filter_mails(mail)
        ]

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
