#Tuple
# It is a like a list, that is immutable
my_tuple = (1,2,3,[4,5,6]) # tuple()
# my_tuple.append(4) #creates an error because it cannot be added to a tuple
my_tuple[3].append(7)# We can change the elements inside a list if a list is an tuple item so basically we cannot change the tuple item but if the tuple item is a list we can change it because list is mutable
print(my_tuple)

#Set
# We cannot store duplicates
my_set = {1,2,3,4,5,6,7,7}
print(my_set)
my_set.add(8)
my_set.remove(1)
print(my_set)

# Day 4
# Dictionary
# C++ -> un_ordered map of object
# Java -> HashMap of Object, object
# JS -> JS Object with any key type
# 
# A dictionary is a key-value pair
my_dict = {}
my_dict = {"Amar": 42,"Ananya":99,"Surya":42}
my_dict["Ravana"] = 100
my_dict["Amar"] = 99
print(my_dict)
print("Amar" in my_dict.keys())
del my_dict["Surya"]
print(my_dict)

print(my_dict.items())# dict_items([('Amar', 99), ('Ananya', 99), ('Ravana', 100)]) It gives us a tupe list of key and value pair

my_dict_items = list(my_dict.items())
for i in range(len(my_dict_items)):
    item = my_dict_items[i]
    print(f"Key: {item[0]} and Value : {[item[1]]}")

# Type casting means, changing data from type A to type B without changing memory 