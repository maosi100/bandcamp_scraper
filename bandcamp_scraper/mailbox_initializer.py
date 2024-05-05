from abc import ABC, abstractmethod
import mailbox
import email
from email import message
from email import policy
from typing import Optional, List

class MailboxInitializer(ABC):
    @abstractmethod
    def _conect_mailbox(self, filepath: str):
        pass

    def create_mailbox(self, filepath: str):
        pass

class MboxMailboxInitializer(MailboxInitializer):
    def create_mailbox(self, filepath: str) -> List[message.EmailMessage]:
        mailbox = self._connect_mailbox(filepath)
        return [mail for mail in mailbox]

    def _connect_mailbox(self, filepath:str) -> Optional[mailbox.mbox]:
        try:
            return mailbox.mbox(filepath, factory=self._factory_EmailMessage)
        except IsADirectoryError:
            raise IsADirectoryError(f"{filepath} is a directory")

    @staticmethod
    def _factory_EmailMessage(file):
        return email.message_from_binary_file(file, policy=policy.default)
