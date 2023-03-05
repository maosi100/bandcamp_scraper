import mailbox
import email
from email import policy
from re import search
from base64 import b64decode
import json
from datetime import datetime

# Factory to create email.message.EmailMessage instead of mailbox.Message
def make_EmailMessage(file):
    return email.message_from_binary_file(file, policy=policy.default)

def create_database(path):
    # Set up the mailbox using the factory above
    try:
        mbox = mailbox.mbox(path, factory=make_EmailMessage)
    except IsADirectoryError:
        return False
    
    database = []

    for mail in mbox:
        if "release" in mail["Subject"]:
            input = mail.get_body(preferencelist=('html'))

            if "base64" in str(input):
                input_stripped = search("^.+base64(.+)$", str(input).replace("\n", "")) # Strip the header data for proper decoding
                input = b64decode(input_stripped.groups(1)[0]).decode('utf-8')

            if "iso-8859-1" in str(input):
                input_stripped = search("^.+iso-8859-1(.+)$", str(input).replace("\n", ""))
                input = str(input_stripped.groups(1)[0]).encode("utf-8")

            if "just released" in str(input):
                if match := search(r"<a href=\"(.+)\">", str(input)) or search(r"<a href=3D\"(.+)\">", str(input)):
                    url = match.groups(1)
                    database.append([mail["Date"], url[0], "0"])
            

        database.sort(key=lambda x: datetime.strptime(x[0], "%a, %d %b %Y %H:%M:%S %z"))

    json_object = json.dumps(database, indent=4)

    with open("database.json", "w") as outfile:
        outfile.write(json_object)

    return True
