from mailbox_initializer import MboxMailboxInitializer
from mailbox_reader import MailboxReader
from database_creator import DatabaseCreator

class EmailScraper():
    def __init__(self) -> None:
        self.supported_mailbox_types = ["mbox"]
        self.mailbox_initialiazer = MboxMailboxInitializer()
        self.mailbox_reader = MailboxReader()
        self.database_creator = DatabaseCreator()

    def process(self, filepath: str):
        if self.__read_mailbox_type(filepath):
            mailbox = self.mailbox_initialiazer.create_mailbox(filepath)
            extracted_mails = self.mailbox_reader.extract_emails(mailbox)
            self.database_creator.append_entries_to_database(extracted_mails)

    def __read_mailbox_type(self, filepath: str) -> bool:
        if filepath[-4:] in self.supported_mailbox_types:
            return True
        else:
            raise ValueError(f"{filepath} is not a supported filetype")
