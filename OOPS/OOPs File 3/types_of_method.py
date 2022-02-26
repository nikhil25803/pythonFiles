

class Student:

    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+ self.m2+self.m3)/3

    def get_m1(self): # Getters-> Fetch the Value
        return self.m1

    def set_m1(self, value): # Setters -> Updates the value
        self.m1 = value

    @classmethod
    def get_schoo(cls):
        return cls.school # Class method

    @staticmethod
    def info():
        print("This is a Static Method") # Static Method

s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)

print(s1.avg())
print(Student.get_schoo())
Student.info()

# Class method is created to access or operate class variables 

# Static method is created to access variables that are not concerned to class and instance variables 