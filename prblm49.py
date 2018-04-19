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

    #print("List: it took "+str(tock-tick) +" to find the thing")
    lst[:] = (value for value in lst if value != 0)
    return lst;
def permutations(a,b,c):
    stra=str(a)
    strb=str(b)
    strc=str(c)
    if sorted(stra)==sorted(strb)==sorted(strc):
        return True
    else:
        return False
def conc(vec):
    stra=str(vec[0])
    strb=str(vec[1])
    strc=str(vec[2])
    print(stra+strb+strc)
    return stra+strb+strc

def main():
    x=10000
    lst=sieve(x)
    lst = [i for i in lst if i // 1000 > 0]
    nums=[]
    print(len(lst))
    for check in range(1,len(lst)):
        #print(lst[check])

        i=lst[check]+3330
        j=3330+i
        # for i in range(check+1,len(lst)):
        #     for j in range(i+1,len(lst)):
        if permutations(lst[check],i,j) and check!=1:
            nums.append([lst[check],i,j])
    for i in nums:
        conc(i)
    pass
main()
