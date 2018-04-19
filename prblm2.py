init=[1,1]
num=1
i=1
while num<4000000:
    num=init[i]+init[i-1]
    init.append(num)
    i+=1
print(init)
evens=[x for x in init if x%2==0]
print(evens,sum(evens))
