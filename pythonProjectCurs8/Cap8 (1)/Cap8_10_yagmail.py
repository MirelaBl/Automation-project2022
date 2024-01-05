"""
810 Module
Modulul yagmail - exemple
PF - 29.06.2021 v6
"""  #


import sys
sys.path.append("C:\\Users\\admin\\Documents\\__PyThOn\\0 PyP\\_module")  # pt pftp

import pftp  # parola paul
import yagmail

destinatar = 'paul@fratila.eu'
username = 'paulfrtlg@gmail.com'
subject = 'test e-mail / gmail'
mesaj = """Salut Gabriel,

Acesta este un e-mail test la SMTP !

Paul
"""

try:
    server = yagmail.SMTP(username, pftp.parolag)
    server.send(destinatar, subject, mesaj)
    print('Mesaj expediat cu succes!')
except:
    print(str(sys.exc_info()))
    print('Mesajul nu a putut fi expediat!')

# MYACCOUNT.GOOGLE.COM
# SECURITY
# LESS SECURE APP ACCESS ON
