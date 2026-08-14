#Exception Handling

# import datetime


# def divide_two_numbers(a,b):
    # if b == 0:
    #     print("Denominator cannot be 0") # handling such that the exception never occurs
    # else:
    #     return a / b

    # try:
    #     return a / b
    # # except:
    # except ZeroDivisionError as e:
    #     return e
    # except Exception as e:
    #     return e
    # finally:
    #     print("Try completed")

# print(divide_two_numbers(10,0))
# print(divide_two_numbers(10,5))

# class AirtribeException(Exception): #Creating an exception of our own
#     def __init__(self, message):
#         self.message = message
#         self.time = datetime.datetime.now()

# def divide_two_numbers(a,b):
#     try:
#         if a < b:
#             raise AirtribeException("A cannot be less than B") #If not handled it wont be noticed
#         else:
#             return a / b
#     except Exception as e:
#         return e

# print(divide_two_numbers(-10,5))

# Situation 1 - We want to handle the Exception

# def test_func(a,b):
#     try:
#         if a < b:
#             raise AirtribeException("A cannot be less than B") #If not handled it wont be noticed
#         else:
#             return a / b
#     except Exception as e:
#         return e

# print(test_func(-10,5))

# Situation 2 - We do not want to handle the Exception

# def test_func(a,b):
#     """
#     Args:
#         a: First value to compare.
#         b: Second value to compare.
#     Raises:
#         AirtribeException("a is less than b")
#     """
#     if a < b:
#         ex = AirtribeException("A cannot be less than B") #If not handled it wont be noticed
#         raise ex
#     else:
#         return a / b


# def hello(a,b):
#     try:
#         test_func(a,b)
#     except Exception as e:
#         return f"Message - {e.message} \nTime - {e.time}"
# print(hello(-10,5))

# def hello(a,b):
#     try:
#         test_func(a,b)
#     except AirtribeException | ZeroDivisionError as e: #Handles multiple exceptions using the same method at once, e is an object for either airtribe and zero division error and it happens from left to right
#         return f"Message - {e.message} \nTime - {e.time}"
# print(hello(-10,5))


class MyException(Exception):
    pass

class AmarException(MyException):
    pass

class AbhishekException(MyException):
    pass

def test_function(a):
    if a < 0:
        raise AmarException
    if a > 0:
        raise AbhishekException
    print(a)

# def caller(a):
#     try:
#         test_function(a)
#     except (AmarException , AbhishekException) as e:
#         print(f"Amar or Abhishek exception occured - {e}")

def caller(a):
    try:
        test_function(a)
    except MyException as e: # Eventhough child classes of Exception is thrown still it handles the child exception
        print(f"Amar or Abhishek exception occured - {e}")

caller(10)
caller(-10)
caller(0)