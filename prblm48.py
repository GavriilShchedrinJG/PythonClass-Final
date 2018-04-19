x=1000
tot=0
for i in range(1,x+1):
    tot+=i**i
print(tot%10000000000)
