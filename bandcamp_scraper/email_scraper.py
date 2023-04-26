from mailbox_creator import MailboxCreator
from email_url_extractor import EmailUrlExtractor
from email_database import EmailDatabase


class EmailScraper:
    def __init__(self, filepath) -> None:
        mailbox = MailboxCreator().create_mailbox(filepath)
        email_extractor = EmailUrlExtractor(mailbox)
        email_extractor.extract_emails()
        email_database = EmailDatabase(email_extractor.database)
        email_database.sort_database()
        email_database.write_json_from_list()
