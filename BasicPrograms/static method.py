class Employee:
    @staticmethod
    def greet():
        print("Good Morning Sir")
    def getSalary(self, signature):
        print(f"Salary for this Employee is {self.salary}\n{signature}")
    @staticmethod
    def time():
        print("Time is 9 AM in the morning")
harry=Employee()
harry.greet()
# Employee.greet(harry)
harry.salary=100000
harry.getSalary("Thanks !")
harry.time()