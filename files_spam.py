''' 
Write a program to sense spam words
Example Donkey
'''
with open('example.txt') as f:
    content=f.read()

content=content.replace("Donkey",'#$%@#$')

with open('example.txt','w') as f:
    f.write(content)