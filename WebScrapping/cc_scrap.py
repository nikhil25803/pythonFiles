
import requests
from bs4 import BeautifulSoup



page = requests.get("https://www.codechef.com/contests?itm_medium=navmenu&itm_campaign=allcontests")
soup = BeautifulSoup(page.text, 'html.parser')

table1 = soup.find('table')

# print(table1)

for i in table1.find_all('tbody'):
    print(i)