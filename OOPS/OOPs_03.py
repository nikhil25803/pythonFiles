# Use of Constructors
class Item:
    def __init__(self,name,price,quantity):
        print(f"An instances created: {name}")
        
        print(f"Total price is: {price*quantity}\n")



item1 = Item("Phone",100,5)   


item2 = Item("Laptop",1000,3)


