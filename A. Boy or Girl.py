""""
a = input()
b = set()
for word in a.split():
    for char in word:
        b.add(char)
c = len(b)
if c % 2 == 0:
    print ("CHAT WITH HER")
else:
    print("IGNORE HIM!") 
"""

s = input()
distinct_chars = set()
for char in s:
    distinct_chars.add(char)
    print (distinct_chars)
if len(distinct_chars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

