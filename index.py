import os
from imbox import Imbox  # pip install imbox
import traceback
import os
import datetime
from datetime import datetime
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

host = os.getenv('SERVER')
username = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
EXTENSAO = 'pdf'

DOWNDIR = "./download"

if not os.path.isdir(DOWNDIR):
    os.makedirs(DOWNDIR, exist_ok=True)

now = datetime.now()
now.strftime("%Y,%m,%d")

mail = Imbox(host, username=username, password=password,
             ssl=True, ssl_context=None, starttls=False)
messages = mail.messages(date__on=datetime.date(now))  # defaults to inbox

file = []

for (uid, message) in messages:
    mail.mark_seen(uid)  # optional, marks message as read
    for idx, attachment in enumerate(message.attachments):
        try:
            att_fn = attachment.get('filename')

            file = att_fn.split('.')
            if (file[1] == EXTENSAO):
                download_path = DOWNDIR+'/'+att_fn
                print(download_path)
                with open(download_path, "wb") as fp:
                    fp.write(attachment.get('content').read())
        except:
            pass
            print(traceback.print_exc())

    #move mail para a pasta setada.
    mail.move(uid, destination_folder='TechmailBackup')   

mail.logout()