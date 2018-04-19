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
    x=6000
    lst=sieve(x)
    lst.pop(0)
    #print(lst)
    arr=[]
    for i in range(100,x):
        testarr=[]
        teststatement=True
        if(i in lst):
            test=1
        elif(i%2==1):
            for j in range(1,int((x/2)**(0.5))):
                result=i-2*j**2
                testarr.append(result)
            teststatement=any(i in lst for i in testarr)
            if not teststatement:
                arr.append(i)


    print(arr)
    pass
main()
