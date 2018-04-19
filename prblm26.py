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

def f(n, d):
    x = n * 9
    z = x
    k = 1
    while z % d: #and n!=3:
        z = z * 10 + x
        k += 1

    return k, #long(z) / long(d)

def main():
    n=1000
    k0=0
    arr=primes(n)
    #print(arr)
    #print(len(arr))
    k0=f(1,3)
    for i in range(1,len(arr)):

        if arr[i]%5==0:
            continue
        k=f(1,arr[i])
        if k>k0:
            k0=k
            ans=arr[i]
    print(ans)
    pass

#print(f(1,2))
main()
