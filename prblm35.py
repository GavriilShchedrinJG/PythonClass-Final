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

def circular(N,lst):
    num=N
    n=len(str(num))
    bol=True
    while True:
        rem=num%10
        div=num/10
        num=int((10**(n-1))*rem+div)
        if num not in lst:
            bol=False
            break
        if num==N:
            break
    #print("Hey")
    return bol



def main():
    x=1000000
    lst=sieve(x)
    print("run")
    tot=0
    # print(circular(197,lst))
    for i in lst:
        if ( not re.search('[24680]',str(i))):
            if circular(i,lst):
                tot+=1
    print(tot)
main()
