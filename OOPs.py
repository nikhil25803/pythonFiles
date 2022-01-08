# OOPs- Solving by object method
#Use Railway Form
'''
class RailwayForm:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


nikhilApplication=RailwayForm()
nikhilApplication.name="Nikhil"
nikhilApplication.train="Hatia Patna"
nikhilApplication.printData()

class Employee:
    company="Google"
    salary=100 #Object

hrarry=Employee()
rajini= Employee()
print(hrarry.company)
print(rajini.company)

hrarry.salary=300 #Instance attributes
rajini.salary=400 #Instance attributes

Employee.company="YouTube"
print(hrarry.company)
print(rajini.company)
print(hrarry.salary)
print(rajini.salary)
# print(rajini.address) --> this will throw error as 
# there is no such attributes 
'''

#Understanding self()
'''
class Employee:
    comapny="Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")

nikhil=Employee()
nikhil.salary =100000
nikhil.getSalary()
# or
# Employee.getSalary(nikhil)
'''

# Telusko OOPs ---------Class 1------------------------
'''
class Computer:

    def config(self):
        print("i5 16gb 1TB")


com1=Computer()  #indicating which class it belongs

Computer.config(com1)
'''

# print(type(com1)) Class COmputer

# Telusko OOPs ---------Class 2------------------------
'''
class Computer:

    def __init__(self,CPU,Ram):
        # print("in init")
        print

com1=Computer("i5",16)
com2=Computer("Ryzen",16)  
'''
#
'''
class Computer:
    def __init__(self):
        self.name="Navin"
        self.age=18

    def update(self):
        self.age=20

    
c1=Computer()
c2=Computer()

print(c1.name) # Both will have same value
print(c2.name)

c2.name="Nikhil"
print(c2.name) # Now it will print the different value

print(c1.age) #This belong to age


c1.update()
print(c1.age) # and this belongs to updated age

# Compare


# print(id(cl))
# print(id(c2 ))
'''

#Types of variable
'''
class Car:

    wheels=4

    def __init__(self):
        self.mil=10
        self.company="BMW" # Instance Variable
c1=Car()
c2=Car()

print(c1.company,c1.mil,c1.wheels)
print(c2.company,c2.mil)

#Updated Value
c2.mil=20
c2.company="Audi"
print("Updated Value: ",c2.company,c2.mil,c1.wheels)
'''

# Static Method
'''
class Student:

    school="Telusko"


    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2    
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod #Decorators
    def schoolname(cls):
        return cls.school

    @staticmethod # Decorators
    def info():
        print("This is students class: ")

s1= Student(34,67,32)
s2=Student(89,32,20)

print(s1.avg())
print(s2.avg())

print(Student.schoolname())
print(Student.info())
'''

# Class inside a Class
'''
class Student:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.roll)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand="Dell"
            self.cpu="i5"
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student("Nikhil",5)
s2=Student("Raj",9)

s1.show()
lap1=s1.lap
lap2=s2.lap

# print(id(lap1))

lap1=Student.Laptop()
'''

# Inheritance Single and multi level
'''
class A:

    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")

class B(A):

    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")

class C(B): #Inheritance all the value form A and B
            # if B is not inherited from A use class C(A,B)
    pass

a1=A()

a1.feature1()
a1.feature2()

b1=B()

b1.feature3()
b1.feature3()
b1.fe
'''
# Constructor in Inheritance
class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")

class B(A):

    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")



a1=A()
a1.feature1()   #we can acess feature 1  and feature 2 only
a1=B()