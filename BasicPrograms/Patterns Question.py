# Question 1
'''
*****
*****
*****


n=int(input("Enter the number: "))
for i in range(n-2): # i indicates rows
    for j in range(n): # j indicates coloumns
        print("*",end="")

    print()

'''

# Question 2 Hollow Box
'''
* * * * *
*       * 
* * * * *

row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of coloumn: "))

for i in range(0,row):
    for j in range(0,col):
        if (i==0) or (j==0) or (i==row-1) or (j==col-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''

# Question 3

'''
******
*****
****
***
**
*


n=int(input("Enter the number: "))
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()

'''
# Question 3
'''
*
**
***
****
*****

n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

'''

# Question 4 { PYRAMID }
'''
     *
    ***
   *****
  *******
 *********
***********

n=int(input())
for i in range(1,n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i-1),end="")
    print(" "*(n-i-1))
print()
'''

# Question 5 { Reverse Pyramid }
'''
*********
 *******
  *****
   ***
    *

n=int(input("Enter the number of rows: "))
for i in range(n,-1,-1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print(" "*(n-i))
print()
    
'''

# Question 6 [Diamond with consecutive progression]
'''
   *
  * *
 * * *
* * * *
 * * *
  * *
   *


n=int(input("Enter the number: "))

for i in range(n):
    print(" "*(n-i)+" *"*(i+1))
for j in range(n-2,-1,-1):
    print(" "*(n-j)+" *"*(j+1))
print()
'''


# Question 7 [ Diamond with uneven procedding ]


'''
  *
 ***
*****
 ***
  *

row=int(input("Enter the number of rows: "))

for i in range(row):
    print(" "*(row-i),end="")
    print("*"*(2*i+1))
#print()
for i in range(row-2,-1,-1):
    print(" "*(row-i),end="")
    print("*"*(2*i+1))
'''

# Question 8 [ Half Diamond]
'''
*
**
***
****
*****
****
***
**
*

n=int(input("Enter the number: "))

for i in range(1,n+1):
    print("*"*i)
for j in range(n-1,0,-1):
    print("*"*j)
print()

'''

# Question 9
'''
    *
   **
 ****
*****
 ****
  ***
   **
    *

n=int(input("Enter the number: "))

for i in range(n-1,-1,-1):
    print(" "*i+"*"*(n-i))

for j in range(1,n):
    print(" "*j+"*"*(n-j))

print()
'''

# Question 10
'''
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * *

n=int(input("Enter the number: "))

for i in range(n):
    print(" "*i+"* "*(n-i))
for j in range(2,n+1):
    print(" "*(n-j)+"* "*j)
print()
'''

# ----------------------------------------#

# Another type of Pattern { Numbers }

#Question 11
'''
1
12
123
1234
12345
123456


n=int(input("Enter the number: ")) 

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

'''
# Question 12
'''
1
22
333
4444
55555
666666
7777777

n=int(input("Enter the number: "))
 
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()
'''

# Question 12
'''
11111
2222
333
44
5
'''
n=int(input("Enter the number: "))
k=0

for i in range(n,0,-1):
    k+=1
    for j in range(1,i+1):
        print(k,end="")
    print()