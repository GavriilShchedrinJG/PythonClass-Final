def fib(n,v1,v2,v3):
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v1,v2,v3

def index():
    k=[1,3,4,5,6,7]
    v1,v2,v3=1,1,0
    i=0
    print("it poops out after a while but it gets pretty far pretty quick something somthing that much math is hard")
    for j in range(len(k)):
        if j>4:
            while len(str(ans))<(10**k[j]):
                1/(5**0.5)*((1+(5*0.5))/2)**i
                i=i+1
        elif j==3 or j==4 or j==3:
            ans=0
            while ans<(10**k[j]):
                v1,v2,v3=1,1,0
                i=i+1
                v1,v2,v3=fib(i,v1,v2,v3)
                ans=len(str(v2))
                print(ans,i)
            print(i)
        else:
            while len(str(v2))<(10**k[j]):
                v1,v2,v3=1,1,0
                i=i+1
                v1,v2,v3=fib(i,v1,v2,v3)
                #print(v2)
            print(i)
        i=i*10+15

    pass
index()
