a = input()
upper_count = 0
lower_count = 0

for char in a:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

 #print(upper_count , lower_count  )
if upper_count > lower_count:
    print(a.upper())
else:
    print(a.lower())
