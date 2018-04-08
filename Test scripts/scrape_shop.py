from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")

for child in bsObj.find("table",{"id":"giftList"}).descendants:
    print(child)
