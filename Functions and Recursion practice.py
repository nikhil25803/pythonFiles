#Q1-Write a program to print maximum of three numbers

'''
def max(n1,n2,n3):
    if (n1>n2):
        if n1>n3:
            return n1
        else:
            return n3
    else:
        if n2>n3:
            return n2
            
        else:
            return n3

c=max(5,8,2)
print(c)
'''

#Q2-Write a program to convert celcius to farenheight

''''
def faren(c):
    f=(c*9)/5 +32
    return f

c1=faren(20)
print(c1)
'''

#Q3- How to prevent pyhton to print a new line
'''
print("Hello",end=" ")
print("How",end=" ")
print("Are",end=" ")
print("You?",end=" ")
'''

#Q4- Use recursion to find sum of n ntural number
'''
n=int(input())
i=0
for sum in range(1,n+1):
    #print(sum)
    i+=sum
print(i)
'''
#Using recursion
'''
def sum(n):
    if n==1:  # Assume it as a point it gets stopped
        return 1
    return sum(n-1)+n
    
    
s=sum(10)
print(s)
'''

# Write a function to print
'''
***
**
*
'''
''''
n=3
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
'''

# Write a function to print multiplication of a table

def mult(n):
    for i in range(1,11):
        res=n*i
        print(res)

x=int(input())
print(mult(x))