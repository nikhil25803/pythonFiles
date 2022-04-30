# Ques 1
'''
Write a prof=gram using functions to display prime numbers 
between two numbers entered by the user

def prm(x,y):
    # count=0
    l1=[]
    for i in range(x,y+1):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break

        if flag==0:
            l1.append(i)
    return l1
# print()

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
print(prm(x,y))
'''

# Question 2 { Unsolved }

# Input the number to be checked.
# Repeat from i = 2 to (num/2).
# Check if (i) is a prime number.
# If i is prime, check if (n - i) is a prime number.
# If both (i)and (n - i) are primes, 
# then the given number can be represented as 
# the sum of primes i and (n - i).
'''
Write a program to check if an integer can  be expressed
as the sum of two prime numbers, if yes the print all
such combinations { Using Functions }



def sum_of_primes(num):
    isPrime = 1
    for i in range (2,int(num/2),1):
        if(num % i == 0):
            isPrime = 0
            break
    return isPrime

num = int(input("Enter a number : "))
flag = 0;
i = 2
for i in range (2,int(num/2),1):
    if(sum_of_primes(i) == 1):
        if(sum_of_primes(num-i) == 1):
            print(num,"can be expressed as the sum of",i,"and",num-i)
            flag = 1;
if (flag == 0):
    print(n,"cannot be expressed as the sum of two prime numbers")

'''

# Question 4
'''
Write a function to convert Decimal to Binary number
by creating user defined functions


# For in built function

def decimalToBinary(n):
	return bin(n).replace("0b", "")

# Driver code
if __name__ == '__main__':
	print(decimalToBinary(8))
	print(decimalToBinary(18))
	print(decimalToBinary(7))

# using user defined functions

def binary(n):
    # value=0
    l1=[]
    while n!=0:
        temp =n%2
        l1.append(temp)
        # print(temp,end="")
        n=n//2
        l1.reverse()
    return l1

n=int(input())
print(binary(n))
'''
# Question 5
'''
Write a program to convert binary number
into decimal number

# def decimal(binary)
n=int(input())
i=0
value=0
while (n!=0):
    temp= n%10
    temp=temp*(2**i)
    i=i+1
    value=value+temp
    n=n//10
    # return value

print(value)
'''