import smtplib

from email.mime.text import MIMEText

with open ('dummy.txt') as fp:
    msg = MIMEText(fp.read())

msg['Subject'] = "Tester email"
msg['From'] = "pisterk1@gmail.com"
msg['To'] = "vip.pister@gmail.com"

s = smtplib.SMTP('smtp.gmail.com')
s.ehlo()
s.starttls()
s.login("pisterk1@gmail.com", "password")
s.send_message(msg)
s.quit()
