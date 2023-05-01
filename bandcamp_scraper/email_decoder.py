from abc import ABC, abstractmethod
from base64 import b64decode
from re import search


class EmailDecoder(ABC):
    @abstractmethod
    def decode_email(email_body):
        pass

class Base64Decoder(EmailDecoder):
    @staticmethod
    def decode_email(email_body):
        stripped_body = search("^.+base64(.+)$", email_body.replace("\n", ""))
        return b64decode(stripped_body.groups(1)[0]).decode('utf-8')

class Iso88591Decoder(EmailDecoder):
    @staticmethod
    def decode_email(email_body):
        replaced_body = email_body.replace("\n", "").replace("3D", "")
        stripped_body = search("^.+iso-8859-1(.+)$", replaced_body)
        return str(stripped_body.groups(1)[0]).encode("utf-8")
