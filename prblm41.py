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
    #we know if the digit sum of a number is divisible by 3 then the number is divisible by 3
    #this rules out all pandigital primes except with 4 and 7 pandigital primes
    x=10000000
    lst=sieve(x)
    ans=[]
    for num in reversed(lst):
        i=str(num)
        if ('1'in i and '2'in i and '3'in i and '4'in i and '5'in i and '6'in i and '7'in i):
            ans.append(i)
            break


    print(ans)
    return
main()
