from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
# print(tbody)

trs = tbody.contents
# print(trs)
# print(list(trs[0].children))

prices = {}

# for tr in trs[:10]:  # Name all the cryptocurrency
#     name, price = tr.contents[2:4]
#     fixed_name = name.p.string
#     print(fixed_name)

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    # print(price.a.string) # For price

    prices[fixed_name] = fixed_price

print(prices)

# Output - 
# {'Bitcoin': '$41,000.45', 'Ethereum': '$2,911.73', 'Tether': '$1.00', 'BNB': '$396.50', 'USD Coin': '$0.9996', 'XRP': '$0.8119', 'Terra': '$94.61', 'Cardano': '$0.8975', 'Solana': '$89.18', 'Avalanche': '$87.91'}