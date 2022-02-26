# Use of Constructors and specifying data types

class Item:

    def __init__(self,name: str,price: int,quantity: int):
        
    
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        
        return self.price*self.quantity
        

item1 = Item("Phone",100,2)   
print(item1.total_price())

item2 = Item("Laptop",1000,3)
print(item2.total_price())
