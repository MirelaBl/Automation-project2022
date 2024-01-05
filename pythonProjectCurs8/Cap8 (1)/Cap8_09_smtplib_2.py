"""
809 Module
Modulul smtplib - exemple
PF - 29.06.2021 v6
"""  #


import sys
sys.path.append("C:\\Users\\Default\\Documents\\__PyThOn\\0 PyP\\_module")    # pt pftp

#import pftp
import smtplib

expeditor = 'bmirela306@gmx.at'
destinatar = 'mirela.blaschke@gmail.com'
username = 'bmirela306@gmx.at'
subiect = 'ceva'
mesaj = """From: {0}
To: {1}
Subject: {2}
Content-type: text/html
<html>
Salut,
 	<head>
		<title></title>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
		<link href="../../../default.css" rel="stylesheet" type="text/css" />
	</head>
	<body style="background:none;margin:0px">
 	    <h1 class=jobstitle>TEST test</h1>
	</body>
<p>Paul</p>
</html>
""".format(expeditor, destinatar, subiect)

parola= '123test123test123'
print(expeditor, destinatar, subiect);
try:
	smtp_ob = smtplib.SMTP('mail.gmx.com:587')
	smtp_ob.starttls()  						# protocol criptare
	smtp_ob.login(username, parola)
	for i in destinatar:
		smtp_ob.sendmail(expeditor, i, mesaj)
		print(f'Mesaj to {i} expediat cu succes!')
	smtp_ob.close()

except:
		print(f'Mesajul  expediat catre {expeditor} de catre {destinatar} nu a putut fi expediat!')
