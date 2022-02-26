# Use of Constructors

class Item:

    def __init__(self,name,price,quantity=0):
       
        self.name = name
        self.price = price
        self.quantity = quantity

   
        

item1 = Item("Phone",100)   
print(item1.name)
print(item1.price)
print(item1.quantity)

item2 = Item("Laptop",1000)
print(item2.name)
print(item2.price)
print(item2.quantity)

