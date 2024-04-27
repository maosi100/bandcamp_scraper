from mailbox_reader import MailboxReader
from database_creator import DatabaseCreator

class ScrapeProcessor:
    def __init__(self, filepath: str) -> None:
        self.mailbox = MailboxReader(filepath)
        self.database = DatabaseCreator(self.mailbox.extracted_mails)
