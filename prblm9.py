
def g(x,n):
    ret=(x*x+1)%n
    return ret;
def gcd(a,b):
    while b!=0:
        remainder=a%b
        a=b
        b=remainder
    return a;
def pythag(x):
    val=1000
    A=0
    B=0
    C=0
    cnt=0
    for i in range(50,x):
        a=i
        for j in range(i+1,x):
            b=j
            c=(b**2+a**2)**0.5

            if(c.is_integer()):
                #print(a,b)
                cnt=cnt+1

                if(a+b+c==val):
                    A=a
                    B=b
                    C=c
                    break

    print(A,B,C,A+B+C)
    ans=A*B*C
    print(cnt)
    print(ans)
    return;
def main():
    pythag(int(500))
    return;
main()
