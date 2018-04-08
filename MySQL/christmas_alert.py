import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "christmas_alerts@signh.no"
    msg["To"] = "karramsos@gmail.com"

    s = smtplib.SMTP("localhost")
    s.send_message(msg)
    s.quit()

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"), "lxml")
while(bsObj.find("noscript").string == "NEI"):
    print("It is not Christmas yet.")
    time.sleep(3600)
    bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"), "lxml")

sendMail("It's Christmast", "According to https://itischristmas.com, it is Christmas!")

