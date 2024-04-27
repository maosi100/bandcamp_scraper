from mailbox_reader import MailboxReader
from database_creator import DatabaseCreator
from database_handler import DatabaseHandler

class ScrapeProcessor:
    def __init__(self, filepath: str) -> None:
        self.mailbox = MailboxReader(filepath)
        self.database = DatabaseCreator(self.mailbox.extracted_mails)
