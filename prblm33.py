
#solving (10*n+i)/(10*i+d)=n/d)
#then reduce the fraction suing the greated common denominator of the numerator and denominator

def gcd(a,b):
    while b!=0:
        remainder=a%b
        a=b
        b=remainder
    return a;

den=1
nom=1

for i in range(1,10):
    for d in range(1,i):
        for n in range(1,d):
            if ((n*10+i)*d==n*(i*10+d)):
                den *=d
                nom *=n

print(den/gcd(nom,den))
