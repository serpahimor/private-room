
from bs4 import BeautifulSoup
with open('test-bs4.html',"r") as html:# automatic close the file
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
    print(type(soup.title))
    print(soup.title.string)
    print(soup.head)
    print(soup.p)