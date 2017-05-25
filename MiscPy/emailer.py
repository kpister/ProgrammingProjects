import smtplib

from email.mime.text import MIMEText

pw = open("pw.txt").readline()
pw.strip()

with open ('dummy.txt') as fp:
    msg = MIMEText(fp.read())

msg['Subject'] = "Tester email"
msg['From'] = "pisterk1@gmail.com"
msg['To'] = "sanjeev96red@gmail.com"

s = smtplib.SMTP('smtp.gmail.com')
s.ehlo()
s.starttls()
s.login("pisterk1@gmail.com", pw)
s.send_message(msg)
s.quit()
