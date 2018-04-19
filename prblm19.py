totsun=1

mon=[31,28,31,30,31,30,31,31,30,31,30,31]
day=0
for i in range(1901,2001):
    for j in mon:
        day+=j
        if i%4==0 and j==28:day+=1
        if day%7==0:totsun+=1
print(totsun)
