# Class Attribute and __dict__ method

class Item:

    pay_rate = 0.8 # The pay rate after 20% discount

    def __init__(self,name: str,price: int,quantity: int):
        # Run validation to receive arguments
        assert price >= 0 ,f"Price {price} can not be negative"
        assert quantity >= 0, f"Quantity can not be negative"
        
        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity


    def total_price(self):
        
        return self.price*self.quantity

    def apply_discount(self):
        
        self.price = self.price * self.pay_rate
        

item1 = Item("Phone",100,5)   
item1.apply_discount()
print(item1.price)


item2 = Item("Laptop",1000,3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

