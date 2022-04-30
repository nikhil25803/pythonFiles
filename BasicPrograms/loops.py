#Understandiing Loops

#While Loops
'''
i=0
while i<=10:
    print("Yes " + str(i))
    i=i+2
print("Done")
'''

#Write a program to print from 1-50
'''
n=1
while n<=50:
    print(n)
    n=n+1
print("Done")
'''


#print content of alist

'''
fruits=['Banana', 'Watermelon', 'Orange', 'Pomogranate','Pineapple']
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1
'''

#FOR LOOPS 

#print list using for loop
'''

fruits=['Banana', 'Watermelon', 'Orange', 'Pomogranate','Pineapple']

for item in fruits:
    print(item)

'''

# RANGE in Python
'''

for i in range(8):
    print(i)
   
'''

#using range(start, stop, step size)
'''
for j in range(1,10,2):
    print(j)
    
'''

#ELSE i for loop
'''
for i in range(10):
    print(i)
else:
    print("DONE")

'''

# BREAK Statement
'''
for i in range(10):
    print(i)
    if i==5:
        break
         #loop will stop at 5 only
''' 

#CONTINUE Statement
'''
for i in range(10):
    
    if i==5:
        continue
    print(i)
        #this program will skip 5
'''

#PASS Statement
i=4
 if i>0:
     pass

print("Nikhil")
































































