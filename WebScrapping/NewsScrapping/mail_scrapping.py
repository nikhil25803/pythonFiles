from bs4 import BeautifulSoup
import urllib.request as urllib2
import re

html_page = urllib2.urlopen("https://groups.google.com/a/heritageit.edu.in/g/aiml25/members")
soup = BeautifulSoup(html_page)
links = []

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))

print(links)