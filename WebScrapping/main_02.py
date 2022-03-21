import imp
from textwrap import indent
import requests

from bs4 import BeautifulSoup

url = "https://www.newegg.com/Processors-Desktops/SubCategory/ID-343"

result = requests.get(url)

# print(result.text)

doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify())

prices = doc.find_all(text="$")
parent = prices[0].parent
# print(parent)

strong = parent.find("strong")
print(strong.string)