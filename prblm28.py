def squares(x):
    arr=[]
    n=1
    for i in range(x):
        arr.append(n**2)
        n=n+2
    #print(arr)
    return arr
def sums(arr):
    some=0
    for i in range(1,len(arr)):
        for j in range(4):
            some=some+arr[i]-(i+i)*j
    some=some+1
    return some

def main():
    arrsize=1001
    length=round(arrsize/2+0.2)
    #print(length)

    arr=squares(length)
    some=sums(arr)

    print(some)
    return

main()
