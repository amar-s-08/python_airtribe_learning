# Object Oriented Programming
# Class
# FOR TEA we need to decide the following:
# 1. Type of tea -> [Milk,Green,Lemon,Black]
# 2. Contains Ginger -> True/False
# 3. Contains Sugar -> True/False
# 4. Contains Spices -> True/False
# 5. Size -> Tall/Grand/Venti
# Object

class Tea:
    # In Python a constructor is represented by the __init__ method
    def __init__(self,tea_type,contains_ginger,contains_sugar,contains_other_Spices,size="Tall"):
        self.tea_type = tea_type
        self.contains_ginger = contains_ginger
        self.contains_sugar = contains_sugar
        self.contains_other_spices = contains_other_Spices
        self.size = size
    

brahmesh_tea = Tea("MILK",True,True,False,"Grande")
basant_tea = Tea("Lemon",True,False,False,"Venti")

print(brahmesh_tea.tea_type)
print(basant_tea.tea_type)
# print(basant_tea) # Won't work it gives output -> <__main__.Tea object at 0x109cec410>