# Use recursion to find sum of N natural number
'''
def sum_recur(n):
    if n==0:
        return 0
    return n+sum_recur(n-1)
    

n=int(input("Enter the number: "))
print(sum_recur(n))
'''

# Write a program to calculate factorial of a number
'''
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

n=int(input("Enter the number: "))
print(fact(n))
'''

#  Write a program to find GCD of two numbers
'''
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b=map(int,input().split())
print(gcd(a,b))
'''

import math

# Write a program to print power of a number where 
# base and exponent is entered by the user

'''
def power(a,b):
    return math.pow(a,b)

x,y=map(int,input().split())
print(power(x,y))
'''
