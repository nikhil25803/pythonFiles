class Vehicle: # Parent Class

    def __init__(self, milage, cost):
        self.milage = milage
        self.cost = cost

    def show_vehicle_details(self):
        print("I am a Vehicle")
        print("Milage of the vehicle is: ", self.milage)
        print("Cost of the vehicle is: ", self.cost)
v1 = Vehicle(300,500)

class Car(Vehicle):

    def __init__(self,milage,cost,tyres,hp):
        super().__init__(milage, cost)
        self.tyres = tyres
        self.hp = hp

    def show_car_details(self):
        print("I am Car")
        print("Number of tyres are: ", self.tyres)
        print("Value of horsepower is: ",self.hp)

c1 = Car(20,12000,4,1000)
c1.show_car_details()