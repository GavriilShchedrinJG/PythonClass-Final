import re
def sieve(x):
    lst=[1 for i in range(x)]
    #print(lst)
    lim=round(x**0.5+0.5)
    for i in range(2,lim):
        if lst[i]==1:
            j=i**2
            while (j<x):
                lst[j]=0
                j=j+i

    #print(lst)
    cnt=0
    for i in range(0,len(lst)-1):
        if lst[i]==1:
            cnt=cnt+1
            lst[i]=i

    lst[:] = (value for value in lst if value != 0)
    return lst;

def check(num,lst):
    bol=False
    for i in range(1,len(str(num))):
        num1=int(str(num)[i:])
        num2=int(str(num)[:i])
        #print(num1,num2)
        if num1 not in lst or num2 not in lst:
            return False
    return True


def main():
    x=900000
    lst=sieve(x)
    ans=[]
    n,f=11,1
    lst.pop(0)
    #print(lst[-1])
    # check(3539,lst)
    while len(ans)<11:
        n+=3-f
        f=-f
        if (n>1 and not re.search('[4680]',str(n))):
            if n in lst and check(n,lst):
                ans.append(n)
                print(n)
    print(ans)
    print(sum(ans))
    return
main()
