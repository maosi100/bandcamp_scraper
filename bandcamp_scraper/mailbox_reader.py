import mailbox
import email
from email import policy

class MailboxReader():
    @staticmethod
    def read_mailbox(filepath: str) -> mailbox.mbox:
        if not filepath.endswith('.mbox'):
            try:
               return mailbox.mbox(filepath, factory=MailboxReader._factory_EmailMessage)
            except IsADirectoryError:
                raise IsADirectoryError(f"{filepath} is a directory")
    
    @staticmethod
    def _factory_EmailMessage(file):
        return email.message_from_binary_file(file, policy=policy.default)
