from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://static.norges-bank.no/contentassets/b36f0051784546c5a56ce612036e9c4c/ppr_2_2017_tall.htm?v=06/22/2017140842&ft=.htm")
bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj.prettify)


<a href="http://static.norges-bank.no/contentassets/b36f0051784546c5a56ce612036e9c4c/ppr_2_2017_tall.xlsx?v=06/22/2017140827&amp;ft=.xlsx">Tallsett</a>