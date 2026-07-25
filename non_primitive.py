# Data Structures - for all languages

# 1. Arrays -> A continuous memory is allocated - hence it always starts from 0
# int -> 4 bytes | [22,23,21,22,24] - Array of type int
# ["Shantanu","Amar","Nishanth"] - Array of type String
# [True,False,True,True] - Array of type boolean
# In languages like Java, an Array has a fixed type and a pre-defined size
# int [] array = new int[5]; [0][0][0][20][0] -> 5 * 4 = 20 bytes only integer is allowed Array is homogenous
# index 0 1 2 3 4 | array[3] -> 20
# index will always starts with 0 and it can't be changed
# M213-starting memory address           0 1 2 3 4 
# [][][][][]  ||[][][][][] || [][][][][][][][][][][][]
#               array
# array[0] = M213
# array[1] = M213 + 1 = M214

# 2. Linked List

# [] -> [] -> [] -> [] -> X
# It is not a continuous memory allocation
# A linked list is also a homogenous in nature. It doesn't have a fixed size.
# In a LL, we store 2 things
# 1. The Value
# 2. The address to the next value

# If we want to read the continuously and heavily Array should be used instead of Linked List

# In browser the previous and forward can be used to implement in linked list
# For Array we can have real world example would be cart We can access the item any number of times and it will be fast and instantaneous

# 3. String -> Ultimately, aa string is a character array.
# A string is immutable. immutable means it can't be changed.
# first_name = "Ama" -> ['A']['m']['a']
# last_name = "S" -> ['S']
# first_name = first_name + "r" -> ['r'] | ['A']['m']['a']['r']
# first_name points to the new array list with ['A']['m']['a']['r']


# 4. Stack -> LIFO (Last In First Out)
# Start: [1][2][3] 
# remove top element -> [1][2]
# add 1 element -> [1][2][4]
# 
# 5. Queue -> FIFO (First In First Out)
# Start: [1][2][3][4] : END
# remove [1] gets removed
#
# # 6. Set -> A set is a like a list, but it cannot contain duplicates.
# set -> [1,1,1,1,2,2,2,2,2] -> [1,2]
#  
# In Python -> Array + Linked List + Stack + Queue = All of these are represented as a List.

# from collections import deque

# my_stack = deque()# Double ended Queue

# List as a Stack
# push -> add | pop -> remove

# my_stack = []
# my_stack.append(10)
# my_stack.append(20)
# Removing an element of stack = Removing the last added element //[10,20,30,40,50] -> my_stack[4] X
# print(my_stack[len(my_stack) - 1])
# print(my_stack[-1])
# print(my_stack[-2])
# print(my_stack.pop())
# print("My Stack after popping",my_stack)

# List as a Queue
# enqueue/offer -> add | dequeue -> remove

# queue = []

# queue.append(10)
# queue.append(20)
# print(queue)
# item = queue.pop(0)
# print("My Queue after deQueue ",queue)

# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# l1.extend(l2)
# print(l1)

nums = [10,20,30,40,50]
# print(nums[-1])
# print(nums[-2])
# print(nums[-3])

# Slicing
# Python supports slicing using syntax:
# list[start:stop:step] -> start - Include | stop - Exclude | step = 1 (by Default)

# print("SLicing: ",nums[1:4])
# print("Slicing: ",nums[:3])
# print("Slicing: ",nums[:])# this creates a new list example instead of taking the same one
# print("Reverse Slicing : ",nums[::-1])
# print("Reverse Slicing : ",nums[-2:-4:-1])#[40, 30] -> Reverses and goes from 2nd position to 4th where 2nd is included and 4th is excluded
print("Before Slicing and updating ",nums) #[10,20,30,40,50]
nums[1:4] = [200,300]
print("After updating the sliced contents : ",nums)#[10,200,300,50] -> contents from 1st index to 4th is removed and has been updated by the new items.
