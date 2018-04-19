
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
            if(cnt==10003):
                print(i)
            lst[i]=i
    lst[:] = (value for value in lst if value != 0)
    return lst;
def main():
    x=2000000
    lst=sieve(x)
    lst.pop(0)
    print(sum(lst))
    return
main()
