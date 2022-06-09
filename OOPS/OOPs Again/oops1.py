# Position, name, Salary


# sel1 = ['SDE', "Nikhil", 2000]
# sel2 = ['SDE2', 'Kusumita', 50000]
# d1 = ["Designer", "Philip"]

# def code(se, de):

#     print(f"{se[1]} is writing code for {de[1]}")

# code(sel1, d1)


# Class
from zmq import Again


class SoftwareEngineer:

    # Class atrribute
    alias = "Amazon"

    def __init__(self, name,  salary):

        # Instance attributes
        self.name = name
        self.salary = salary

    # Methods

    def work(self):

        print(f"{self.name} is working for {self.alias} at salary {self.salary}")

    def salary(self):

        print(f"{self.name} is working at salary {self.salary}")

    # Other Dunder methods

    def __str__(self):
        return f"Name: {self.name}\nSalary: {self.salary}\nCompany: {self.alias}"

    # Compare two objects
    def __eq__(self, other):
        return self.name == other.name and self.salary == other.salary

    def entry_fees(self, new_salary):
        if self.age < 15:
            new_salary == 4500
            print(f"{self.salary} is changed because age {self.age}")

        if self.age < 30:
            new_salary == 5000
            print(f"{self.salary} is allocated because age {self.age}")


# Instance
se1 = SoftwareEngineer("Nikhil", 14, 2000)
se2 = SoftwareEngineer("Raj", 31, 2000)
se1.entry_fees()
