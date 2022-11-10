from imbox import Imbox
import traceback
import os
import datetime
from datetime import datetime


def downloadxlsxmail(MAILHOST, MAILUSER, MAILPASS, DOWNDIR, EXTENSAO):
    if not os.path.isdir(DOWNDIR):
        os.makedirs(DOWNDIR, exist_ok=True)

    now = datetime.now()
    now.strftime("%Y,%m,%d")

    mail = Imbox(MAILHOST, username=MAILUSER, password=MAILPASS,
                 ssl=True, ssl_context=None, starttls=False)
    # defaultsfaults to inbox
    messages = mail.messages(date__on=datetime.date(now))

    file = []

    for (uid, message) in messages:
        mail.mark_seen(uid)  # optional, marks message as read
        for idx, attachment in enumerate(message.attachments):
            try:
                att_fn = attachment.get('filename')

                file = att_fn.split('.')
                if (file[1] == EXTENSAO):
                    download_path = DOWNDIR + '/' + att_fn
                    print(download_path)
                    with open(download_path, "wb") as fp:
                        fp.write(attachment.get('content').read())
            except:
                pass
                print(traceback.print_exc())

    mail.logout()
