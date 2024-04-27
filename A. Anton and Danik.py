b = input()
z = input()
a = 0
d = 0
for i in z: 
    if  i == 'A'  :
        a = a + 1
    elif i == 'D' :
        d = d + 1     
if a > d : 
    print ("Anton")
elif d > a :
    print ("Danik")
elif a == d :
    print("Friendship")
