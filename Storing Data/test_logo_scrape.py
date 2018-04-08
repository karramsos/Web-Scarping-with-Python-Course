from bs4 import BeautifulSoup
from urllib.request import urlopen
soup = BeautifulSoup(urlopen('http://www.singh.no').read())
logo = soup.find("img", {"id": "logo"})["src"]
print(logo)

'''for x in soup.find_all(id='logo'):
    try:
        if x.name == 'img':
            print (x['src'])
    except:pass
    '''