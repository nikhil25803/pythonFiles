# 'a' here symbolise append
f=open('file_name.txt','a') 

line1 = f.write("\nThis is the entered line")
print(line1)

f.close() 

# Output1 --> 
# Hello world
# This is Python !

# #Read first line
# data=f.readline()
# print(data)

# #Read second line
# data=f.readline()
# print(data)

# #Read third line
# data=f.readline()
# print(data)

# #Read the fourth line
# data=f.readline()
# print(data)

# This will print the first line
# print(f.read())