from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

#wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
document = ZipFile("CV_Sukhvinder_Singh_9feb17_rev.docx")
#wordFile = BytesIO(wordFile)
#document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

wordObj = BeautifulSoup(xml_content.decode('utf-8'), "lxml")
textStrings = wordObj.findAll("w:t")
for textElm in textStrings:
    print(textElm.text)