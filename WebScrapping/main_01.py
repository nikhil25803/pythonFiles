from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


# print(doc.prettify)

tag = doc.title
# print(tag.string)

tag.string = "Hello" # Title will get replaced by Hello
# print(doc) 

tags = doc.find_all("p")[0] # Access Tags
print(tags.find_all("b"))