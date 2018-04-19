
def primesq(n):
    arr=[]
    p=0
    for j in range (2,n):
        if n%j==0:
            p=1
            ans=0
    if p==0:
        ans=1
    return ans

def quads(a,b,n):
    x=n**2+a*n+b
    #print(x)
    p=primesq(x)
    return p

def primes(n):
    arr=[]
    for i in range(2,n):
        p=0
        for j in range (2,i):
            if i%j==0:
                p=1
        if p==0:
            arr.append(i)
    return arr
def main():

    a=-79
    b=1601
    p=1
    maxn=1
    maxa=0
    maxb=0
    barr=primes(1000)
    #print(barr)
    for a in range (-501,1000,2):
        for j in range(1,len(barr)):
            b=barr[j]
            p=0
            n=-1
            if -(maxn**2+a*maxn)<b:
                p=1
                #print("check",a,b,maxn)

            while p==1 and b>-(n**2+a*n):
                n=n+1
                p=quads(a,b,n)

            if n>maxn:
                maxa=a
                maxb=b
                maxn=n
    print(maxa,maxb,maxn,"product",maxa*maxb)
    pass

#print(f(1,2))
print(primesq(64))
main()
