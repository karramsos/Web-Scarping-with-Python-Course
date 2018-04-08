from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.singh.no")
bsObj = BeautifulSoup(html, "lxml")
imageLocation = bsObj.find("img", {"id": "logo"})["src"]
urlretrieve (imageLocation, "logo2.jpg")