'''
marks1=[45,78,86,77]
per1=(sum(marks1)/400)*100

marks2=[75,98,88,78]
per2=(sum(marks2)/400)*100

print(per1,per2)
'''

#This can not be used for 
# large file acess

'''
def percent(marks):
    return((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

marks1=[45,78,86,77]
p1=percent(marks1)

marks2=[75,98,88,78]
p2=percent(marks2)

print(p1,p2 )

'''

# Write afumction to greet  a user good day

'''
def greet(name):
    print("Good Day "+ name)

greet("Nikhil")
'''

# Types of Functions
# Built in Function
# User defined Functions

#Functions with argument

def mySum(num1,num2):
    return(num1+num2)

s=mySum(88,12)
print(s)