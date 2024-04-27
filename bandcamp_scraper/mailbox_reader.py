import mailbox
import email
from email import policy

from email_decoder import EmailDecoder

class MailboxReader():
    def __init__(self, filepath: str) -> None:
        self.mailbox = self.connect_mailbox(filepath)
        self.extracted_mails = []
        self.extract_emails()

    def connect_mailbox(self, filepath: str) -> mailbox.mbox:
        if not filepath.endswith('.mbox'):
            try:
               return mailbox.mbox(filepath, factory=self._factory_EmailMessage)
            except IsADirectoryError:
                raise IsADirectoryError(f"{filepath} is a directory")
    
    @staticmethod
    def _factory_EmailMessage(file):
        return email.message_from_binary_file(file, policy=policy.default)

    def extract_emails(self) -> None:
        for mail in self.mailbox:
            if "release" in mail["Subject"]:
                my_dict = {}
                my_dict["Date"] = mail["Date"]
                my_dict["Body"] = self._decode_mails(mail.get_body(preferencelist=('html')).as_string())
                self.extracted_mails.append(my_dict)

    def _decode_mails(self, mail: str) -> str:
        return EmailDecoder(mail).decode()
