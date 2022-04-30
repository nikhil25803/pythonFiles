import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.hindustantimes.com/'
data = requests.get(url)

my_data = []

soup = BeautifulSoup(data.text, 'html.parser')
# articles = html.select('a.post-card')

content = soup.find_all('h3', class_='hdg3')

print(content)