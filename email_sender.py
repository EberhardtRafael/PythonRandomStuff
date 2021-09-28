import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("$HOME/Work/Programming/Python/Email/index.html").read_text())

email = EmailMessage()
email['from'] = 'Mochila'
email['to'] = 'crianca.mochila@gmail.com'
email['subject'] = 'You won $ 1000,000,00'

email.set_content(html.substitute(nome = "Cu do Cu"), 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('crianca.mochila@gmail.com', 'mochila_1999')
	#for i in range(5):
	smtp.send_message(email)
	print("Funcionou.")
