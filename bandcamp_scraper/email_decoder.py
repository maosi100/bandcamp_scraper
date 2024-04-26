from base64 import b64decode
from re import search


class EmailDecoder():
    def __init__(self, mail: str):
        self.mail = mail

    def decode(self) -> str:
        if "base64" in self.mail:
            self.mail = self.decode_base64(self.mail)
        if "iso-8859-1" in self.mail:
            self.mail = self.decode_iso8859(self.mail)
        return self.mail
    
    @staticmethod
    def decode_base64(email_body: str) -> str:
        stripped_body = search("^.+base64(.+)$", email_body.replace("\n", ""))
        return b64decode(stripped_body.group(1)).decode('utf-8')
    
    @staticmethod
    def decode_iso8859(email_body: str) -> str:
        replaced_body = email_body.replace("\n", "").replace("3D", "")
        stripped_body = search("^.+iso-8859-1(.+)$", replaced_body)
        return str(stripped_body.group(1))
