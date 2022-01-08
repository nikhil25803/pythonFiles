class Employee:
    company="Google" 

    def __init__(self, name, salary, subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created: ")

    def getDetails(self):
        print(f"The name of the Employee is {self.name}")    
        print(f"The salary of the Employee is {self.salary}")    
        print(f"The subunit of the Employee is {self.subunit}")

    @staticmethod
    def greet():
        print("Good Morning Sir")

    def getSalary(self, signature):
        print(f"Salary for this Employee is {self.salary}\n{signature}")
    
    @staticmethod
    def time():
        print("Time is 9 AM in the morning")

harry=Employee("Harry",1000, "YouTube")
harry.getDetails()