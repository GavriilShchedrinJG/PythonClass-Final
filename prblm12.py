def sumfactors(x):
    sqrt=x**(0.5)
    sums=1
    arr=[]
    if (sqrt).is_integer():
        arr.append(int(sqrt))
        sqrt-=1
    for i in range(2,int(sqrt)+1):
        if x%i==0:
            #print(i,int(x/i),sums)
            arr.append(i)
            arr.append(int(x/i))
    return arr

num=1
length=1
i=7000
while length<500:
    num=int((i*(i+1)/2))
    #num=76576500
    #num=70012800
    arr=sumfactors(num)
    length=len(arr)
    print(num)
    i+=1
print(len(arr),num)
