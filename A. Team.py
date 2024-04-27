n = int(input())
counter = 0 
for i in range (0 , n ): 
    k = input()
    if k.count ('1') >= 2 :
        counter +=1 
    i += 1 
   
print( f"counter = { counter } " )
