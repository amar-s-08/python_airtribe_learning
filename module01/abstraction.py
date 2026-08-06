"""
Abstraction is an OOP priciple of hiding implementation details and exposing only the essential functionality to the user 

The idea is:
1. Show what an Object does
2. Hide how it does it. 
"""

from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def manufacturer_name(self):
        return "TATA"

class PEngine(Engine):
    @override
    def start(self):
        super().start() # This will call the start method of the parent class and we need to use the child class to call it using super()
        print("Starting Petrol Engine")

    @override
    def stop(self):
        print("Stopping Petrol Engine")

    def start_of_parent(self):
        super().start()

class DEngine(Engine):
    # pass
    @override
    def start(self):
        print("Starting Diesel Engine")

    @override
    def stop(self):
        print("Stopping Diesel Engine")

class EEngine(Engine):
    @override #This is optional even if it is not written it works the same way
    def start(self):
        print("Starting Electrical Engine")

    @override
    def stop(self):
        print("Stopping Electrical Engine")

"""
1. You can create an object of an Abstract class
2. An abstract class can contain methods that are either
    2.a) Abstract/Virtual
    2.b) Non-Abstract (normal)
"""

# e = Engine() # Creates an error 

de = DEngine()
de.start()