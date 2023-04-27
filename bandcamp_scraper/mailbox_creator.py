import mailbox
import email
from email import policy, message
from typing import IO, Any


class MailboxCreator:
    @staticmethod
    def make_EmailMessage(file: IO[Any]) -> message.Message:
        return email.message_from_binary_file(file, policy=policy.default)
    
    def create_mailbox(self, path: str) -> mailbox.mbox:
        try:
            return mailbox.mbox(path, factory=self.make_EmailMessage)
        except IsADirectoryError:
            exit("mbox is a directory")
