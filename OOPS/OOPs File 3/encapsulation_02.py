
class SomeClass:
    
    def public(self):
        print("Public Function")

    def __private(self):
        print("Private Function")

obj = SomeClass()
obj.public() # Calling Public Class
obj._SomeClass__private() # Method to call private class/method

