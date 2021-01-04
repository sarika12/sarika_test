import re
from bs4 import BeautifulSoup

import requests as req


resp = req.get("https://en.wikipedia.org/wiki/Wikipedia")

content =resp.text
# print (content)
soup = BeautifulSoup(content,'lxml')
length=soup.find_all('a')
print("count of <a>",length)
# get content of achor teg
for i in soup.find_all('a'):
    print(i.text)
