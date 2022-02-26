# Make a list of all  the items

class Item:

    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # List to append in

    def __init__(self,name: str,price: int,quantity: int):
        # Run validation to receive arguments
        assert price >= 0 ,f"Price {price} can not be negative"
        assert quantity >= 0, f"Quantity can not be negative"
        
        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute regarding List
        Item.all.append(self)


    def total_price(self):
        
        return self.price*self.quantity

    def apply_discount(self):
        
        self.price = self.price * self.pay_rate
        

item1 = Item("Phone",100,5)   
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75,5)


# print(Item.all)
for instance in Item.all:
    print(instance.name)
    
