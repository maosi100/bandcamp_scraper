import mailbox
import email
from email import policy


class MailboxCreator:
    @staticmethod
    def make_EmailMessage(file):
        return email.message_from_binary_file(file, policy=policy.default)
    
    def create_mailbox(self, path: str):
        try:
            return mailbox.mbox(path, factory=self.make_EmailMessage)
        except IsADirectoryError:
            return False
