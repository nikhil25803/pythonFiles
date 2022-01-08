with open('example.txt','r') as f:
    a=f.read()

with open('example.txt','w') as f:
    a=f.write("Hello") # This will update the file
print(a)