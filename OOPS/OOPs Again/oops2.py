# Inheritance, extend, override
# Process by which one enables to use methods of other


class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working at the age of {self.age}")


class SoftwareEngineer(Employee):

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(
            f"Our Software Engineer {self.name} of age {self.age} and Level {self.level} is Debugging for Salary {self.salary}")


class Designer(Employee):

    def draw(self):
        print(
            f"Our Designer {self.name} is Designing for salary {self.salary}")


se = SoftwareEngineer("Nikhil", 18, 5000, "Junior")
# print(se.debug())
se.debug()

de = Designer("Nikhil", 18, 5000)
# print(de.draw())
de.draw()
