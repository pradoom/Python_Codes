#Sets are mutable it can change

store_sets = {23,342,32.4578,"hello",True}
print("SET 1:",store_sets)
data = {9,8,7,6,65,4,43,3,3}
print(data)
# Sets for branch-wise products
branch_a_products = {"bread", "milk", "butter", "jam"}
branch_b_products = {"bread", "cheese", "butter", "ketchup"}
 
# Print initial sets
print(branch_a_products)
print(branch_b_products)
#ERROR :TypeError: 'set' object does not support item assignment
#branch_a_products[0] = "hello"
branch_a_products.add("hello")
branch_a_products.remove("hello")
print("PRINTING DEFERENACE:",branch_a_products.difference(branch_b_products))
 
# Union of both branches
print(branch_a_products | branch_b_products)
 #op : {'cheese', 'jam', 'butter', 'milk', 'ketchup', 'bread'}
# Intersection of both branches
print(branch_a_products & branch_b_products)
#op {'butter', 'bread'}
# Products only in branch A
print(branch_a_products - branch_b_products)
 # op : {'jam', 'milk'}
# Check if 'ketchup' is in branch A
print("ketchup" in branch_a_products)
 # op False
# Define unmodifiable essential items
essential_items = frozenset(["milk", "bread", "ketchup"])
print(essential_items)
# op :frozenset({'bread', 'ketchup', 'milk'})
#ERROR:WE can not add in FROZEN SET
#essential_items.add("bhgkdk")

#----------------Dictionary-------------------#
store_dic = {"name":"Pradoom","surname":"Rao","age":"27","Eduation":"B.E"}
print(store_dic)

print(store_dic["age"])

for key in store_dic.keys():
    print("keys_NAMES:",key)

for value in store_dic.values():
    print("values:",value)

for key,value in store_dic.items():
    print(f"Keys:{key} values {value}")
num = 34
match num:
    case 12:
        print("12")
    case 34:
        print("34")
    case 99:
        print("other")



#enum example use case in for loop


#List of name
names=["pradoom","punit","abhisheak","durgesh"]


#for loop using enum
for index,name in enumerate(names,0):
    print(f"Index and Name {index}: {name}")