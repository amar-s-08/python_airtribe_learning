# # English meaning of poly is many and morphism is form so polymorphism means many forms

# # Polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated as if they were instances of the same class.

# # Polymorphism is often implemented through inheritance and method overriding.

# # Polymorphism is a powerful concept that allows for code to be written in a more flexible and reusable way.

# # Polymorphism is a key concept in object-oriented programming.

# # Example 1
# # a = 5
# # b = 10
# # c = a + b # + is used to add numbers
# # print(c) # prints 15

# d = "Hello"
# e = "World!"
# f = d + e # + is used to concatenate strings
# print(f) # prints HelloWorld!

# # + is used to add numbers and concatenate strings so it is a polymorphic operator

# # Example 2
# class Dog:
#     def sound(self):
#         print("Bark!")

# class Cat:
#     def sound(self):
#         print("Meow!")

# class Cow:
#     def sound(self):
#         print("Mooo!")

# def animal_sound(animal):
#     animal.sound()

# dog = Dog()
# cat = Cat()
# cow = Cow()

# animal_sound(dog)
# animal_sound(cat)
# animal_sound(cow)


# def add_numbers(a,b):
#     return a + b

# def add_numbers(a,b,c):
#     return a + b + c

# def add_numbers(a,b,c,d):
#     return a + b + c + d

# print(add_numbers(5, 6, 1)) # Polymorphism doesn't occur it throws an error that d variable is not present


# class Employee:
#     def details(self,name):
#         print("The name is : "+name)
    
#     def details(self,name,age):
#         print(f"The name is {name}, and age is {age}")

# e = Employee()
# e.details("Ravana")
# e.details("Ravana",21)

# In python the last function name gets the precedence gets the priority instead of the first one so the first function gets ruled out so polymorphism does not occur

# def add_numbers(a,b,c = 0,d = 0): #Now it will work for even 2 numbers
#     return a + b + c + d

# print(add_numbers(5, 6, 1)) # To achieve polymorphism in python keep the last function with maximum parameters and set the elements which may not occur at the end define it with default values
# print(add_numbers(5, 6))
# print(add_numbers(5, 6, 10))
# print(add_numbers(5, 6, 10,15))

# class Employee:
#     def details(self,name,age=None):
#         if age is not None :
#             print(f"The name is {name}, and age is {age}")
#         else:
#             print(f"The name is {name}")

# e = Employee()
# e.details("Ravana")
# e.details("Ravana",21)

# There are 2 types of polymorphism
# 1 - Runtime polymorphism - Function overriding
# 2 - CompileTime polymorphism - Function overloading

