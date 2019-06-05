# bring in libraries we need
import nltk
from bs4 import BeautifulSoup
from urllib import request

# store the URL we're using
url = "https://usmcourses.org/cms150/"

# grabbing & reading html from URL using urlopen function in request (imported)
html = request.urlopen(url).read()

#took the URL and turned it into a soup object so I can process it
soup = BeautifulSoup(html, 'lxml')
print(soup)
