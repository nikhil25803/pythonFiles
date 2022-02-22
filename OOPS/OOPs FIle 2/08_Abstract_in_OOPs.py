# Methods that have declaration but not definition is called Abstract method and class that have abstract method is called Abstract Class

# We need to import a module to access this

from abc import ABC, abstractclassmethod, abstractmethod

class Computer(ABC):
    @abstractclassmethod # Decorator

    def process(self):
        # print("Running")
        pass

class Laptop(Computer):

    # pass
    def process(self):
        print("Process")

# Instantiate Object
lap = Laptop()
lap.process()
# lap.process

# Abstraction is defined as the process of handling comolexity by hiding unnecessary information from the user. This is one of the core concepts of object-oriented programming(OOP) languages