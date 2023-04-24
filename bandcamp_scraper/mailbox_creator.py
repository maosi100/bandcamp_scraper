import email
from email import policy
import mailbox

class Mailbox:
    def __init__(self, path) -> None:
        self.mailbox = self.create_mailbox(path)
    
    @staticmethod
    def make_EmailMessage(file):
        return email.message_from_binary_file(file, policy=policy.default)
    
    def create_mailbox(self, path: str):
        try:
            mbox = mailbox.mbox(path, factory=self.make_EmailMessage)
        except IsADirectoryError:
            return False
        
        return mbox
