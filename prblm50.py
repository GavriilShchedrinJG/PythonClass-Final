import time

def sieve(x):
    tick=time.time()
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
    tock=time.time()
    #print("List: it took "+str(tock-tick) +" to find the thing")
    lst[:] = (value for value in lst if value != 0)
    return lst;


def main():
    x=1000000
    lst=sieve(int(x))
    lst.pop(0)
    init=0
    c=-1
    ans=[]
    #print(lst)
    maxc=0
    for i in range(100):
        init=0
        c=0

        for i in lst:
            init=init+i
            c+=1
            if(init<x and init in lst and c>maxc):
                ans.append([c,init])
                if c>maxc:
                    maxc=c
        lst.pop(0)
    print(ans)
    print(max(ans, key=lambda x: x[0]))

    return;
main()
