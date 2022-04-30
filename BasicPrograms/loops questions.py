#Question 1
'''
1.Write a program to calculate sum on first
n natural number entered by the user

# Using for loop
n=int(input("Enter the number: "))
i=0
for sum in range(1,n+1):
    i+=sum
print(i)

# Using while loop
n=int(input("Enter the value: "))
sum=0
while n>=0:
    sum+=n
    n-=1
print(sum)
'''

# Question 2
'''
Write a program to find factorial of a
number entered by the user

def facto(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    
    return fact

n=int(input("Enter the number: "))
if n<0:
    print("Incorrect input")
elif n==0:
    print("The value of {} factorial is".format(n)," 1")
else:
    print("The value of {} factorial is".format(n),facto(n))
    
'''

# Question 3
'''
Write a program to print the multiplication
table of n entered by the user

n=int(input("Enter the number: "))


for i in range(1,11):
    tab=n*i
    print(n ," X"," ", i, "=",tab)
'''

# Question 4
'''
Write a program to print fibonacci sequence
till nth term etered by the user

# Iterative approach

def fiboiter(n):
    preValue=0
    currentValue=1
    for i in range(1,n):
        ppValue=preValue
        preValue=currentValue
        currentValue=ppValue+preValue
    return currentValue

n=int(input("Enter the number: "))
print(fiboiter(n))


# Recursive Approach

def fibRecur(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibRecur(n-1)+ fibRecur(n-2)

n=int(input("Enter the value: "))
print(fibRecur(n))

#Using list
def fib(n):
    li=[0,1]

    for i in range(2,n+1):
        next=li[-1]+li[-2]

        li.append(next)
    return li

n=int(input("Enter the value: "))
li=fib(n)
print(li)
'''


# Question 5 
'''
Write a program to print Fibonaci sequence
upto a a certain number


n=int(input("Enter the limit: "))
x,y=0,1
print(x,end=" ")
while y<=n:
    print(y,end=" ")
    x,y=y,x+y
'''

#Question 6
'''
Write a program to find HCF and LCM of two 
nummber entered by the user

# For HCF/GCD
a=int(input())
b=int(input())
la=[]
lb=[]
for i in range(1,a+1):
    if (a%i==0):
        la.append(i)
        c=max(la)
    #return c

for j in range(1,b+1):
    if (b%i==0):
        lb.append(j)
        d=max(lb)
    #return d

    if c==d:
        print("The HCF is {}".format(c))
'''

# For LCM
'''

def lcm(x,y):

    if x>y:
        g=x
    else:
        g=y
    while(True):
        if (g%x==0) and (g%y==0):
            lcm=g
            break
        g+=1
    return lcm

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(lcm(a,b))
'''

#Question 7
'''
Find the sum of digitts of number
entered by the user

inp = [int(i) for i in str(input("Enter a number:"))]
print(inp)


i=int(input("Enter the sum of numbers: "))
sum=0
while (i>0):
    sum=sum+i%10 #remainder value of i gets stored in sum and gets added simultaneoulsy
    i=i//10
print(sum)
'''


#Question 8
'''
Write a program to reverse a number entered by the user


n=int(input("Enter the number: "))
rev=0

while (n>0):
    rev=(rev*10)+n%10 #(0*10)+ (i%10)
    n=n//10

print(rev)
'''

#Question 9

'''
Write a program to calculate power of number 
with and without in built function

# With pow function
import math
def power(a,b):
    c=math.pow(a,b)
    return c

x=int(input("Enter the base value: "))
y=int(input("Enter the exponential value: "))

print(int(power(x,y)))


# Without pow function

def pow(a,b):
    c= a**b
    return c

x=int(input("Enter the base value: "))
y=int(input("Enter the exponential value: "))
#print(int(pow(x,y)))
print("{} to the power {} is {}".format(x,y,pow(x,y)))
'''

# Question 10
'''
Find weather the number entered is palindrome or not


#Method 1 { case sensitive } For string
str=input("Enter the word: ")
strrev=str[-1::-1]
if str==strrev:
    print("Yes! the word {} is a Palindrome".format(str))
else:
    print("No! the word {} is not a Palindrome".format(str))

# Method 2 [For numbers]
num=int(input("Enter the number: "))
temp=num
rev=0
while num>0:
    rev=(rev*10)+num%10
    num=num//10

#print(rev) #Till here we have reversed the code

if rev==temp:
    print("Yes")
else:
    print("No")
'''
#Question 11
'''
Write aprogram to check weather the number entered
is prime or not

n=int(input("Enter the number: "))
prime=True
for i in range(2,n):
    if n%i==0:
        prime=False
        break

if prime:
    print('Prime')
else:
    print('Not Prime')
'''
# Question 12
'''
Write a program to prime numbers between 
two given numbers

x=int(input())
y=int(input())

for i in range(x,y+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break

        else:
            print(i,end=" ")
'''

# Question 13
'''
Write a program to check if anumber is Armstrong
number or not

num=input("Enter the number: ")
temp1=int(num)

l1=[int(j) for j in num]    # Seperate the digits of the input number in a list
#print(l1)

n=len(l1)
l2=[]               # Make another list of operated value of each index of first list  
for i in range(n):
    c=l1[i]**n
    l2.append(c)
#print(l2)

x=sum(l2)   # Find the sum of new list
#print(x)

temp2=int(x)    #Both input and new sum value must be type casted into integer to be compared
#print(temp1,temp2)

if temp1==temp2:
    print("Yes ! the number {} is an Armstrong number".format(num))
else:
    print("No ! the number {} is not an Armstrong  number".format(num))
'''


#Question 14
'''  
Write a program to find the factors of a number
entered bu yhe user

  
n=int(input("Emter the number: "))
factors=[]
for i in range(1,n+1):
    if n%i==0:
        #print(i,end=" ")
        factors.append(i)

print("The factors of the number {} are ".format(n),factors)
'''