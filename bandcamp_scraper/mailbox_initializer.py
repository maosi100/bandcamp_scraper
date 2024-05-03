from abc import ABC, abstractmethod
import mailbox
import email
from email import policy
from typing import Optional

class MailboxInitializer(ABC):
    @abstractmethod
    def connect_mailbox(self, filepath: str):
        pass

class MboxMailboxInitializer(MailboxInitializer):
    def connect_mailbox(self, filepath:str) -> Optional[mailbox.mbox]:
        try:
            return mailbox.mbox(filepath, factory=self._factory_EmailMessage)
        except IsADirectoryError:
            raise IsADirectoryError(f"{filepath} is a directory")

    @staticmethod
    def _factory_EmailMessage(file):
        return email.message_from_binary_file(file, policy=policy.default)
