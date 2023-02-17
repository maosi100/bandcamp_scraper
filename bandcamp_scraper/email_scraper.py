import mailbox
from email import policy
from email.parser import BytesParser

mbox = mailbox.mbox("~/Desktop/TestMailbox.mbox/mbox", factory=BytesParser(policy=policy.default).parse)
mail = mbox.get_message(1)

for part in mail.walk():
    print(part.get_payload())

# for part in mail.walk():
#     print(part.get_message(1).get_payload())    
# print(mbox.get_message(1).get_payload())

# mbox = mailbox.mbox("~/Desktop/TestMailbox.mbox/mbox")
# for part in mbox.get_message(1).walk():
#     print(part.get_message(1).get_payload())
