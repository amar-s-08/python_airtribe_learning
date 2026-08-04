# # All the properties of a parent will inherit to the children
# class Parent:
#     # something
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def print_name(self):
#         print("inside Parent class")


# # Do not use extend we just put a bracket and tell the parent class details
# class Child(Parent):
#     # somethings
#     pass
#     def have_tea(self):
#         print("having Tea")

# p = Parent("Vikrant Poojary", 30)
# c = Child("Vijay Poojary", 5)
# # c = Child() If parent expects 2 parameters it is mandatoy for child as well


# p.print_name()
# c.print_name()
# c.have_tea()
# # p.have_tea() # Is not possible because child can inherit parent's property but parent cannot inherit childs property
# print(p.name)
# print(c.age)

# from typing import override


# class Engine:

#     NAME = "ROLLS ROYCE" # IT is a static variable almost all variables in a class 
#     __privateName = "Private Name"

#     def start(self):
#         print("Starting Engine")

#     def stop(self):
#         print("Stopping Engine")
    
#     def get_private_name(self):
#         return self.__privateName

#     @staticmethod
#     def hello():
#         print("Hello")

# class PEngine(Engine):
#     @override
#     def start(self):
#         super().start() # This will call the start method of the parent class and we need to use the child class to call it using super()
#         print("Starting Petrol Engine")

#     @override
#     def stop(self):
#         print("Stopping Petrol Engine")

#     def start_of_parent(self):
#         super().start()

# class DEngine(Engine):
#     @override
#     def start(self):
#         print("Starting Diesel Engine")

#     @override
#     def stop(self):
#         print("Stopping Diesel Engine")
# class EEngine(Engine):
#     @override #This is optional even if it is not written it works the same way
#     def start(self):
#         print("Starting Electrical Engine")

#     @override
#     def stop(self):
#         print("Stopping Electrical Engine")

# pe = PEngine()
# pe.start()
# pe.stop()

# de = DEngine()
# de.start()
# de.stop()

# ee = EEngine()
# ee.start()
# ee.stop()

# engine = Engine()

# # Function overriding/Method overriding - If the child and parent have same method/function and if the child is calling the same method/function then the priority will be given to child instead of parent

# print(pe.NAME)
# print(de.NAME)
# print(ee.NAME)

# print(Engine.NAME)
# print(PEngine.NAME)
# print(DEngine.NAME)

# # print(pe.__privateName)#This won't work because it is a private variable but we cacn create a getter function and use that variable
# print(pe.get_private_name())#This will work because it is a public function
# print(ee.get_private_name())
# Engine.hello()
# # hello() # This won't work because it is a static method and we need to call it using the class name

# pe.start_of_parent()#This will call the start method of the parent class and we need to use the child class to call it using super()

#Multiple Inheritance - If a class inherits from multiple classes then it is called multiple inheritance

class Parent1:
    def test(self):
        print("Parent1")

class Parent2:
    def test(self):
        print("Parent2")

class Child(Parent2, Parent1): #In python it choses left to right order to inherit the class
    # def test():
    #     print("Child")
    pass

c = Child()
c.test() # Prints Parent2 because it is the left most class in the inheritance chain