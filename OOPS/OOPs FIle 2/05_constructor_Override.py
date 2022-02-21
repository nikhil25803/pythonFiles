class Vehicle: # Parent Class

    def __init__(self, milage, cost):
        self.milage = milage
        self.cost = cost

    def show_vehicle_details(self):
        print("I am a Vehicle")
        print("Milage of the vehicle is: ", self.milage)
        print("Cost og the vehicle is: ", self.cost)

v1 = Vehicle(50,5000)
# v1.show_vehicle_details()

# Child Class

class Car(Vehicle): 
    # Inheriting the Vehicle Class
    def show_car_details(self):
        print("I am a Car")

c1 = Car(200,2000)
c1.show_vehicle_details() 
c1.show_car_details()