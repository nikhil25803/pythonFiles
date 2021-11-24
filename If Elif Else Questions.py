#Question 1
'''
Write a program to check wheather the number is 
Odd or Even

n=int(input())
if n%2==0:
    print("The number is Even")
else:
    print("The number is ODD")

'''

# Question 2
'''
Write a program to check a character is 
vowel or consonant

a=input()
v=['a','e','i','o','u']
if a in v:
    print("The character is a Vowel")
else:
    print("The character is a Consonant")

'''

# Question 3
'''
Write a program to find largest number among
three inputs by the user

#Method 1
a=int(input())
b=int(input())
c=int(input())
val=[a,b,c]
print(max(val))


#Method 2
a=int(input())
b=int(input())
c=int(input())

if (a>b) and (a>c):
    print("Largest number is:",a)

elif (b>a) and (b>c):
    print("The largest number is ", b)
else:
    print("the largest number is ",c)

'''

# Question 4 ***
'''
Write a program which accepts the coefficients
of a quadratic equation from the user and display
roots both real and complex

Hint- Use discriminant formula

#Method 1
a=int(input("Enter coefficient of x^2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the constant value:"))
import math
D=math.sqrt(b**2 - 4*a*c)
d1=(-b+D)/2*a
d2=(-b-D)/2*a
print("The roots are: ",d1,d2)


#Method 2 --> For complex roots also !!
import math

def roots(a,b,c):

    D=math.sqrt(b**2 - 4*a*c)
    
    if D>0:
        
        x=(-b+D)/(2*a)
        y=(-b-D)/(2*a)

        print("The real roots and idstinct roots are {} and {}".format(x,y))
    elif D==0:

        z=(-b/2*a)
        print("The real and equal roots is {}".format(z))

    else:
        print("Roots are complex")
        print((-b)/(2*a)," +i",D)
        print((-b)/(2*a)," -i",D)

a=int(input())
b=int(input())
c=int(input())

if a==0:
    print("Icorrect input")
else:
    roots(a,b,c)
'''

#Question 5
'''
Write a program to check wheather the entered 
year is leap or not.

y=int(input("Enter the year: "))
if (y%2==0) or (y%100==0):
    print("Yes ! the year {} is Leap.".format(y))
else:
    print("Sorry ! the year {} is not leap".format(y))
'''