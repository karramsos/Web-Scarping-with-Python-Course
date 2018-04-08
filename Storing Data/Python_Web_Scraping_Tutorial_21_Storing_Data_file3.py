from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.sukhcoaching.com")
bsObj = BeautifulSoup(html, "lxml")
imageLocation = bsObj.find("img", {"id": "logo"})["src"]
urlretrieve (imageLocation, "logo3.jpg")