class Car:
    wheels = 4 # Class Variable or Static Variable

    def __init__(self):
        self.mil = 50
        self.comp = "BMW"  # Instance Variable

car1 = Car()
car2 = Car()    # Instantiating Objects

car2.comp = "AUDI"
car2.mil = 40

print(car1.mil, car1.comp, Car.wheels)
print(car2.mil, car2.comp, Car.wheels)


# Updating instance variable only affects the objects it is changed for, but changing class variable affects all the object created for that class