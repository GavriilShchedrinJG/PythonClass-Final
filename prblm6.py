def sumsquares(x):
    s=0
    for i in range(0,x+1):
        s+=i**2
    return s
def squaresum(x):
    s=0
    for i in range(0,x+1):
        s+=i
    s=s**2
    return s
def main():
    x=100
    #print(sumsquares(x))
    print(squaresum(x)-sumsquares(x))

    return
main()
