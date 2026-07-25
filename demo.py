#let x = 5
#nameOfVariabler = valueOfVariable
# x = 5
# print(x)

# a = 5
# b = 10
# sum = a + b
# print(sum)

# If the sum is > 10 then print sum, otherwise print -> Sum is less than 10
# a = 10
# b = 10
# sum = a + b

#Conditional Programming - if and else. The "if" should contain a condition that resolves into a boolean

# if sum >10:
#     print(sum)
# else:
#     print("Sum is less than 10")

# if sum > 10:
#     print(sum)
# elif sum < 0:
#     print("Sum is less than 0",sum)
# else:
#     print("Sum is between 0 and 10")

# if sum > 15:
#     print(sum)
# if sum > 10:
#     print("Sum is less than 0",sum)
# else:
#     print("Sum is between 0 and 10")

# if sum > 15:
#     print(sum)
# elif sum > 10:
#     print("Sum is less than 0",sum)
# else:
#     print("Sum is between 0 and 10")

# department = "ECE"

# match department:
#     case "CSE":
#         print("Computer Science and Engineering")
#     case "ECE":
#         print("Electronics and Communication Engineering")
#     case "EE":
#         print("Electrical Engineering")
#     case "ME":
#         print("Mechanical Engineering")
#     case _:
#         print("Unknown Department")

# Functions aka Methods
# y = f(x) | y = x * x -> y is a function of x
# y is the dependent variable and x is the independent variable
# f is the name of the function

# y = square(x)
# square(x) = x * x
# square(4) = 4 * 4 = 16

# In python we write:
#def <name-of-the-function>(<independent-variable-name>):
#    <body-of-the-function>
#    return <dependent-variable-name>

# def square(x):
#     sq = x * x
#     print("The square of", x, "is", sq)
#     return sq
#     print("After return statement") #This statement will not be executed because it is unreachable

# y = square(4)
# print(y)

# Loop
# 1. We know the number of times we want to repeat
# FOR LOOP

#Syntax:
# for<condition>: [run the loop as long as the condition is True, this usually involves the known number]
# ...loop body ...
#The value of i starts from 0 and keeps on incrementing unitl 5, i = 0 -> i = 1 -> i = 2 -> i = 3 -> i = 4 -> i = 5 (stop does not execute) 
# range is (start,stop,skip)
# We can have negative number in parameter
# for i in range(5, 10,2): 
#     print("Ravana ", i)

# for i in range(5,0,-1):
#     print("Reverse Number ", i)

# for i in range (10):
#     if(i == 3):
#         continue
#     elif(i == 4):
#         break
#     else:
#         print(i)

# 2. We don't know the number of times we want to repeat | this can be used when we know the no of times also
# WHILE LOOP
# i = 0
# while i < 15:
#     print("Ravana ",i)
#     i += 1

# secret_number = 7
# guess = 0

# while guess != secret_number :
#     guess = float(input("Guess the number: ")) #int fails when we give float number but if we use float int will also get exact output

# print("Correct Guess")
