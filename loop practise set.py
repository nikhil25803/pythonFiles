#Q.Write aprogram to print the table of a number
'''
n=int(input())
for i in range(1,11):
    print(str(n)+"X"+str(i)+"="+str(i*n))
'''


#Q2> greet all the person in the list whoose name starts with S
'''
l1=["Harry", "Shubham", "Sachin", "Rahul"]
for name in l1:
    if name.startswith("S"):
        print("Hello "+ name)
'''

#Q3> Check a number is prime or not
'''
n=int(input())
prime=True
for i in range(2,n):
    if (n%i==0):
        prime=False
        break
if prime:
    print("Prime")
else:
    print("Not Prime")
'''

#Q>4 Write a program to find sum of first numbers using while loop
'''
n=input()
sum=0
i=1
while i<=n:
    sum=sum+i
    print(sum)
''' 
    


#Q>4 Write the value of n factorial
'''
n=int(input())
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)
'''




























