

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        self._salary = 5000 # ._ is called protected attribute

        self._num_bugs_solved = 0 # __ is for private attribute

        # Getters
        def get_salary(self):
            return self._salary

        # Setters
        def set_salary(self, value):
            self._salary = value
            

se = SoftwareEngineer("Max", 25)
print(se.age, se.name)