# Use a CSV File to store and fetch the value and Static Method
import csv

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


    # Decorator
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = int(item.get('price')),
                quantity = int(item.get('quantity')),
            )
            # print(item)

    @staticmethod
    def is_integer(num):
        # We will  count out the floats that are point zero eg 
        if isinstance(num, float):
            # Count out floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
        
print(Item.is_integer(4.0))
