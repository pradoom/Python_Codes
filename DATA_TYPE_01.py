#Mutable means things that can change
#Immutabe means thing that can not chnage

#Tupples are Immutable, ones declare it can not chnage
#Example
Store_tupple = ("hello","rao","laptop",2457)
#This line creage ERROR, Because trpples are immutable
#Store_tupple[0]="green"
count=Store_tupple.count("hello")
print(Store_tupple[0],count)
print("Compintion:",Store_tupple)

#List are mutanle, we can change it

data = [1,2,3,4,5,6]
data[0]=10

#[10, 2, 3, 4, 5, 6]
print(data)
data.append(56)
print(data)
data.extend([23,43,55,222,1])
print(data)
# data.clear()
# print(data)
data_copy=data.copy()
print("data_copy:",data_copy)
count=data.count(10)
print(count)
#Have to pass element and return index value
print("Index_funtion:",data.index(1))
#Have to pass index to which value to remove
data.pop(2)
print("AFTER POP:",data)
#Have to pass element name which have to remove
data.remove(1)
print(data)
#Reverse the list
data.reverse()
print(data)
#sort the list
data.sort()
print(data)
combine = [1,"hello",2.36478,True]
print(combine)
# string to list
string = "tomato cucumber spinach"
list = string.split()
print(list)


#operator Overloading
data_2 = [1,2,3,4,5]
data_3 = [6,7,8,9]
data_4 = data_2 + data_3
data_4 = data_4*2
print(data_4)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]