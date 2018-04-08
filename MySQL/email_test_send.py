import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = "An Email Aller"
msg["From"] = "sukhvinder@singh.no"
msg["To"] = "karramsos@gmail.com"

s = smtplib.SMTP("localhost")
s.send_message(msg)
s.quit()