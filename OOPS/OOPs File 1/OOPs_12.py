# When to use CLass Method and Static Method

class Item:
    @staticmethod

    def is_integer():
        # It should do something that has a relationship with the class, but not something that must be unique per instances
        pass

    @classmethod

    def instantiate_from_something(cls):
        pass

# However, those could be also called from instances

item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()
    
