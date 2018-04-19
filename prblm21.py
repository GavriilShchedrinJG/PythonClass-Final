def sumfactors(x):
    sqrt=x**(0.5)
    sums=1
    if (sqrt).is_integer():
        sums+=int(sqrt)
        sqrt-=1
    for i in range(2,int(sqrt)+1):
        if x%i==0:
            print(i,int(x/i),sums)
            sums+=i+int(x/i)
    return sums

totsum=0
maxx=10000
for i in range(2,maxx):
    facsum=sumfactors(i)
    if facsum>i and facsum <= maxx:
        if sumfactors(facsum)==i:
            totsum+=i+facsum
print(totsum)
