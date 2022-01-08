# Question 1
# Create a class programmer for storing information of 
# few programmers working at microsoft 
'''
class Programmer:
    company="Microsoft"

    def __init__(self, name, product):
        self.name=name
        self.product=product

    def getInfo(self):
        print(f"The name of the programmer {self.name} and the product is {self.product}")

harry=Programmer("Harry", "Skype")
harry.getInfo()
Alka=Programmer("Alka", "GitHub")
Alka.getInfo()
'''

# Question 2: Write a class calculator capable of 
# finding square, cube and square root of a number
'''

import math
class Calculator:
    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"The value of square of the number {self.number} is {self.number**2}")

    def cube(self):
        print(f"The value of cube of the number {self.number} is {self.number**3}")

    def squareRoot(self):
        print(f"The value of square root of the number {self.number} is {math.sqrt(self.number)}")

a=Calculator(9)
a.square()
a.cube()
a.squareRoot()
'''


# Question3: Create a class with a class attribute a
# create an object from it and set a directly 
# using object.a=0.
# Does it change attributes?

'''
class Sample:
    a="harry"

obj=Sample()
obj.a="Vicky"
print(Sample.a) # Class attributes doesn not changes
print(obj.a)    # Instance attributes changes

#To change classs attributes
Sample.a="Vicky"
print(Sample.a)
'''

# Question4: Greet user using static method

'''
import math
class Calculator:
    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"The value of square of the number {self.number} is {self.number**2}")

    def cube(self):
        print(f"The value of cube of the number {self.number} is {self.number**3}")

    def squareRoot(self):
        print(f"The value of square root of the number {self.number} is {math.sqrt(self.number)}")

    @staticmethod
    def greet():
        print("Welcome to the best Calculator of the World")
a=Calculator(9)
a.greet()
a.square()
a.cube()
a.squareRoot()
'''

# Write a class TRain which has methods to book a ticket
# , get status(no of seats) and get fare information
# of trains running under Indian Railways
'''
class Train:
    company="Indian Railways"


    def __init__(self, name, status, fare):
        self.name=name
        self.status=status
        self.fare=fare

    def getStatus(self):
        print("*********************")
        print(f"The name of the train is {self.name} ")
        print(f"Number of seats available are {self.status}")
        print("*********************************")

    def fareInfo(self):
        print(f"The price of each Ticket is {self.fare}")
        
    def bookTicket(self):
        if(self.status>0):
            print(f"Your Ticket have been booked! Your seat number is {self.status}")
            self.status=self.status-1
        else:
            print("Sorry the teain is Full")

intercity=Train("Intercity Express 14105", 2, 300)
intercity.getStatus()

intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
'''

#Question6:Can you change self parameters?
# Yes
'''
class Sample:
    
    def __init__(self, name):
        self.name=name

obj=Sample("Harry")
print(obj.name)

'''