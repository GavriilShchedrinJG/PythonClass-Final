def conc(vec):
    ans=""
    for i in vec:
        strg=str(i)
        ans+=strg
    return ans
def prods(init,n):
    arr=[x for x in range(1,n+1)]
    ans=[init*i for i in arr]
    return ans

def pan(number):
    nums=str(number)
    return not bool('1234567890'[:9].strip(nums))

def main():
    ans=[]
    i=9
    n=5
    for i in range(0,10000):
        for n in range(1,5):
            templist=prods(i,n)
            tempsort=(sorted(templist, key=str, reverse=True))
            strg=conc(tempsort)

            if pan(strg)and len(strg)<10:
                ans.append(int(strg))
    print(sorted(ans,key=int,reverse=True)[1])
    return
main()
