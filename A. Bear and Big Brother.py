# 3 , 2

a, b = map(int,input().split())
years = 0
# 3x1y>2*x2y
# 
while a<=b:
    years+=1 
    a*=3
    b*=2

print(years)