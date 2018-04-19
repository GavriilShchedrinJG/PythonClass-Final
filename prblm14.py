def chain(x):
    if x%2==0:
        return int(x/2)
    else:
        return 3*x+1

#store length in a thing and check if higher number hit it will speed things up

m=1000000

lst=[0 for x in range(0,m+1)]
length=0
for i in range(2,m):
    #print(i)
    num=i
    k=0
    while num!=1 and num>=i:
        k+=1
        num=chain(num)
    lst[i]=(k+lst[num])
    if lst[i]>length:
        length=lst[i]
        number=i
print(lst)
print(length,number)
