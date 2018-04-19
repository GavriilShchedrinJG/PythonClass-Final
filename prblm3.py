def g(x,n):
    ret=(x*x+1)%n
    return ret;
def gcd(a,b):
    while b!=0:
        remainder=a%b
        a=b
        b=remainder
    return a;
def Rollard(x):
    n=x
    x=2
    xf=2
    d=1
    cycle=2
    ans=[]

    while d != n:
        d=1
        count=1
        while (count<=cycle) and (d<=1):
            x=g(x,n)
            d=gcd(x-xf,n)
            count=count+1
        cycle=cycle*2
        xf=x
        if(d!=1):
            ans.append(d)
        n=int(n/d)

    print(ans)
    return;
def main():
    x=input()
    Rollard(int(x))
    return;
main()
