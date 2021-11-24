# Question 1
'''
Q. Write a program to print Hello World

print("Hello World")
'''

#Question 2
'''
Write a program to print integer number entered by user

n=input().split()
print(n,sep="")
'''

#Question 3
'''
Write a program to add, subtract, multiply and divide
(both float and int value) entered by user 

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a+b) # Sum
print(a-b) # Difference
print(a*b) # Multiplication
print(a/b) # Float division value
print(a//b) # Integer division value
'''

# Question 4 {*}
'''
Write a program to find size of int,float,double and char 
of the user input

import os
import sys
i=int()
f=float()
s=str()

print(i.__sizeof__())
print(f.__sizeof__())
print(s.__sizeof__())

#sys.getsizeof(int())
'''

# Question 5
'''
Write  program where user enters teo value 
(Divisor and Dividend) and quoteint and remainder 
is computed.


x=int(input("Enter the Divisor: "))
y=int(input("Enter the Dividend: "))

r=int(y%x)
q=int((y-r)/x)

print("The value quoteint is: ",q)
print("The value of remainder is: ",r)
'''

# Question 6
'''
Write a program to swap to variables

# Method 1 --> Python exclusive
a=int(input())
b=int(input())
print(a,b)

a,b=b,a
print(a,b)

# Method 2--> Universal
a=5
b=6
print(a,b)

a=a+b #11
b=a-b #11-6=5
a=a-b #11-5=6

print(a,b)
'''

#Question 7
'''
Write a program to print ASII value
American Standard Code for Information Interchange

c='z'
print(ord(c))

'''
# Question 8
'''
Write a program to multiply two float value
'''
f1=float(input())
f2=float(input())

print(f1*f2)