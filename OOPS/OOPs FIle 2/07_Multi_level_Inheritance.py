# Parent Class

class Parent:
    def get_name(self, name):
        self.name = name

    def show_name(self):
        return self.name

# Child Class

class Child(Parent):
    def get_age(self, age):
        self.age = age

    def show_age(self):
        return self.age

# Great Grand Child Class

class GrandChild(Child):
    def get_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.gender

gc = GrandChild()
gc.get_name("Nikhil")
gc.get_age(18)
gc.get_gender("Male")

print(f"Name of the candidate is {gc.show_name()}, age is {gc.show_age()} and gender is {gc.show_gender()}")