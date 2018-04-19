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
    print("List: it took "+str(tock-tick) +" to find the thing")
    return;

def sieveset(x):
    tick=time.time()
    xn=x+1
    not_prime=set()
    primes=[]

    for i in range(2,xn):
        if i in not_prime:
            continue
        for f in range(i*2,xn,i):
            not_prime.add(f)
        primes.append(i)

    cnt=0
    for i in range(0,len(primes)-1):
        cnt=cnt+1
        if(cnt==10001):
            print(primes[i])
    tock=time.time()
    print("Set: it took "+str(tock-tick) +" to find the thing")
    #print(primes)
    return

def main():
    x=input("need ~100000 to get right number")
    sieve(int(x))
    sieveset(int(x))
    return;
main()
