"""
Encapsulation is an OOP principle of building data (attributes) and methods that operate on that data into a single class, while restricting direct access to the internal state of the object.

The goal is:
1. Protect an Object's data
2. Control how data is accessed and modified.
3. Hide Implementation dettails from the outside world.
"""

#Example without encapsulation

# class BankAccount:
#     def __init__(self,balance) -> None:
#         self.balance = balance

# acc = BankAccount(1000)
# print(acc.balance)
# acc.balance = -5000
# print(acc.balance)

#Example with encapsulation

# class BankAccount:
#     def __init__(self,balance) -> None:
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount

#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient Amount")
# acc = BankAccount(1000)
# print(acc.balance)
# acc.deposit(500)
# print(f"After deposit {acc.balance}")
# acc.withdraw(300)
# print(f"After withdrawal {acc.balance}")
# acc.balance = -5000
# print(acc.balance)

# Access modification / Access modifier
# 1. Public - ACCESS FROM EVERYWHERE
# 2. Protected [_] - Accessible inside the class and the children [CONVENTION]
# 3. Private [__] - Can't be accesses outside the class

# a class can't be access modified like private or protected


class Student:
    def __init__(self) -> None:
        self.name = "Alice"
        self._marks = 82
        self.__parentNumber = "0987654321"

    def getParent(self):
        return self.__parentNumber
    
    def setParentNumber(self,number):
        self.__parentNumber = number

s = Student()
print(s._marks)
# print(s.__parentNumber)# throws an error because private cannot be accessed

print(s.getParent)

print(s._Student__parentNumber) # It works but is discouraged