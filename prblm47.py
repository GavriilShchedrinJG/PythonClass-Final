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

def Numfact(number,primes):
    nod = 0
    remain = number

    for i in range(0,len(primes)):
        #// In case there is a remainder this is a prime factor as well
        #// The exponent of that factor is 1
        if(primes[i] * primes[i] > number):
            nod+=1
            return nod


        pf = False
        while (int(remain % primes[i]) == 0):
            #print (int(remain % primes[i]))
            pf = True
            remain = remain / primes[i]
        if (pf):
            nod+=1

        #If there is no remainder, return the count
        if (remain == 1):
            return nod

    return nod

def main():
    x=100000
    primes=sieve(x)
    primes.pop(0)
    targetpf=4
    consec=1
    targetconvec=4
    result=2*3*5*7
    arr=[]
    while(consec<targetconvec):
        #print(result)
        result+=1
        if Numfact(result,primes)>=targetpf:
            arr.append(result)
            consec+=1
        else:
            consec=0
            arr=[]
    print(arr)
    return;
main()
