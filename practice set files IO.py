'''
Write a program to read the file poem.txt
and check wheather it have the word
"Twinlke" or not
'''

f=open('poem.txt','r')
t=f.read()
if 'Twinkle' in t:
    print("Present")
else:
    print("No")



f.close()