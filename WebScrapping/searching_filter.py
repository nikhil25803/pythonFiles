# from textwrap import indent4
import re
# import limit
from bs4 import BeautifulSoup

with open("index2.html","r") as f:

    doc = BeautifulSoup(f, "html.parser")


# Rename the tags

# tag['value'] = "new value"
# tag["colour"] = "blue"
# print(tag)

# Find Tags

# tag = doc.find_all(["p", "div", "li"])
# print(tag)

# Find Class Name
# tag = doc.find_all(class_ = "btn-item")
# print(tag)

# Find tag using one symbol

# tags = doc.find_all(text=re.compile("\$.*"), limit=1) # Limit number of search

# for tag in tags:
#     print(tag.strip()) # Remove all the white spaces
# # print(tags)


# Save modified file

tags = doc.find_all("input", type="text")

for tag in tags:
    tag['placeholder'] = "I Changed You"

with open("changed.html", "w") as file:

    file.write(str(doc))