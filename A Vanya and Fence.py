import numpy as np 
"""
my_List = [1,2,3,4,5]
my_array = np.array(my_List)
print(my_List)
print(my_array)
print("-"*25)
print(type(my_List))
print(type(my_array))
print("-"*25)
a = np.array ( 1 )
b = np.array ( [10 , 20 ] )
c = np.array ([ [10,20] , [20,30] ] )
d = np.array([ [ [10,20] , [20,30] ]  ,  [ [30,40] ,[40,50] ] ]) 
print (f"A is : {a}")
print (f"B is : {b}")
print (f"C is : {c}")
print (f"D is : {d}")
print("-"*25)
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print("-"*25)
my_custom_array=np.array ([1,2,3],ndmin=3)
print(my_custom_array)
print(my_custom_array.ndim)
--------------------------------------------------------------------------------------
people = int(input("Enter how many people: "))
bridge = int(input("bridge : "))
num_set = list()
counter = 0
# Get numbers from the user and add them to the set
for i in range(people):
    num = int(input(f"Enter number {i + 1}: "))
    num_set.append(num)
for i in num_set: 
    if bridge >= i :
        counter = counter + 1
    else : counter = counter +2 

print (counter)
"""
x,y = map(int, input().split())
z = list(map(int,input().split()))
counter = 0
for i in z: 
    if y >= i :
        counter = counter + 1
    else : counter = counter +2 

print (counter)

