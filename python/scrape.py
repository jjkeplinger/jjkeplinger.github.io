# bring in libraries we need
import nltk
from bs4 import BeautifulSoup
from urllib import request

# store the URL we're using
url = "https://github.com/humanitiesprogramming/scraping-corpus"

# grabbing & reading html from URL using urlopen function in request (imported)
html = request.urlopen(url).read()

#took the URL and turned it into a soup object so I can process it
soup = BeautifulSoup(html, 'lxml')
our_text = soup.text
links = soup.find_all('a')[0:10]

print(links)

# limited the number of characters
# print(our_text[0:2000])

# replaced line breaks with spaces
# print(soup.text.replace('\n', ' '))


links_html = soup.select('td.content a')
this_link = links_html[0]

urls = []

# adding each link to a new list of processed urls
for link in links_html:
    to_append = (link['href'].replace('blob/', ''))
    urls.append('https://raw.githubusercontent.com' + to_append)

# picking a specific url, i.e., work
#test_url = urls[3]

corpus_texts = []

for url in urls:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)
    print('Scraping' + url)

print(len(corpus_texts))
print(len(corpus_texts[0]))
