'''
There are many in builts function in pythin that we can use 
to access the files in python 
some of them are
'''

#Open a file

f=open('example.txt','r') #use open to read content of a file
#r=read/w=write/ By default read is accessed
# data=f.read()
data=f.read(5) #This will read first 5 character of the text documents
 
print(data)
f.close() 