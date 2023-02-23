import mailbox
import email
from email import policy
from datetime import datetime
from re import search
from base64 import b64decode

# Factory to create email.message.EmailMessage instead of mailbox.Message
def make_EmailMessage(file):
    return email.message_from_binary_file(file, policy=policy.default)

# Set up the mailbox using the factory above
mbox = mailbox.mbox("~/Desktop/Bandcamp all.mbox/mbox", factory=make_EmailMessage)

# Create a list of tuples of date received and mail IDs
# sorted_list = []
# for i, mail in enumerate(mbox):
#     if "release" in mail["Subject"] or "bought" in mail["Subject"]:
#         sorted_list.append((mail["Date"],  i))
# sorted_list.sort(key=lambda x: datetime.strptime(x[0], "%a, %d %b %Y %H:%M:%S %z"))
# # print(sorted_list)
# 
# # Search for release URLs within the sorted Emails
# for item in sorted_list:
#     input = mbox[item[1]].get_body(preferencelist=('html'))
#     
#     # Decode from base64 if required
#     if "base64" in str(input):
#         input_stripped = search("^.+base64(.+)$", str(input).replace("\n", "")) # Strip the header data for proper decoding
#         input = b64decode(input_stripped.groups(1)[0]).decode('utf-8')
#     
#     # Search for URL Link in email body sring
#     if match := search(r"<a href=\"(.+)\">", str(input)):
#         url = match.groups(1)
#         print(*url)

# [{timestamp: YYYY-MM-DD, type: release or follower, body: link or email body}]

database = []
for mail in mbox:
    # if "release" in mail["Subject"]:
    #     input = mail.get_body(preferencelist=('html'))

    #     if "base64" in str(input):
    #         input_stripped = search("^.+base64(.+)$", str(input).replace("\n", "")) # Strip the header data for proper decoding
    #         input = b64decode(input_stripped.groups(1)[0]).decode('utf-8')

    #     if match := search(r"<a href=\"(.+)\">", str(input)):
    #         url = match.groups(1)
    #     
    #     database.append({"Date": mail["Date"], "Type": "Release", "Body": (*url)}) 

    if "bought" in mail["Subject"]:
        input = mail.get_body(preferencelist=('html)'))
        database.append({"Date": mail["Date"], "Type": "Follower", "Body": str(input)})

print(database)
