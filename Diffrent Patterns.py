'''

****
****
****


# Solution

for i in range(4):
    for j in range(4):
        print("* ",end="")
    print()

'''
# Question 2

'''
*
**
***
****


for i in range(4):
    for j in range(i+1):
        print("* ",end="")
    print()

'''

# Question 3

'''
****
***
**
*


for i in range(4):
    for j in range(4-i):
        print("* ",end="")
    print()

'''

#Question 4

'''
    *
   **
  ***
 ****
*****

for i in range(6):
    print(" "*(6-i),end="")
    print("*"*i,end="")
    print(" "*(6-i))
print()

'''

# Question 5

'''
*****
 ****
  ***
   **
    *

for i  in range(5,-1,-1):
    print(" "*(5-i),end="")
    print("*"*(i),end="")
    print(" "*(5-i))
print()

'''

# Question 6

'''
   *   
  ***  
 *****
*******


for i in range(5):
    print(" "*(5-i-1),end="")
    print("*"*(2*i-1),end="")
    print(" "*(5-i-1))
print()

'''

# Question 7

'''
*******
 *****
  ***
   *


for i in range(4,-1,-1):
    print(" "*(4-i),end="")
    print("*"*(2*i-1),end="")
    print(" "*(4-i))
print()
'''

# Question 8   # UNSOLVED
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''

# Question 9
# Write a program to print star of n*n stars(*) such that 
# the center one is always blank

'''
eg
***
* *
***

and

*****
***** 
** **
*****
*****

import math
n=int(input())
a=int(math.floor(n/2))

for i in range(n):
    for j in range(n):
        if i==a and j==a:


            print(" ",end="")
        else:
            print("*",end="")
    print()

'''