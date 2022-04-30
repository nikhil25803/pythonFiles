words=["Donkey","mango","Bihar"]

with open("example.txt") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"#####")

    with open("example.txt","w") as f:
        f.write(content)
