from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "lxml")
    try:
        print("H1: ", bsObj.h1.get_text())
        print("1st paragraph:\n", bsObj.find(id = "mw-content-text").findAll("p")[0])
        print("Edit link: ", bsObj.find(id = "ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('--------------------\n'+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")