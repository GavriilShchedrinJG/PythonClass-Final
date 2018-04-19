
def perm(num,ind):
    if (ind==len(num)-1):
        print(num)
        return
    for i in range(index,len(num)):
        lst=num[:]
        temp=lst.pop(i)
        lst.insert(index,temp)
        perm(lst,index)



digits=[0,1,2,3,4,5,6,7,8,9]

import itertools
digit='0123456789'
k=10
lst=["".join(x) for x in itertools.permutations(digit, k)]
print(lst[1000000-1])
