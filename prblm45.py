
#every hexagonal number is a triangular number so only need to check pentagonal and hexagonal
def shapes(init,x):
    #tri=[]
    # n*(3*n-1)=2*m*(2*m-1)
    # 3*n^2-n=4*m^2-2*m
    # (6*n-1)^2-3*(4*m-1)^2=-2
    #x=6*n-1,y=4*m-1
    #x^2=-2+3*y^2
    m=0
    marr=[]
    narr=[]
    for y in range(init,x):
        x=(-2+3*y**2)**(0.5)
        #if not (x).is_complex():
        if (x).is_integer():
            m=(y+1)/4
            n=(x+1)/6
            if (m).is_integer() and (n).is_integer():
                marr.append(m)
                narr.append(n)

    return marr,narr
def main():
    x=1000000
    init=10000
    marr,narr=shapes(init,x)
    #tripentarr=[x for x in tri if x in Pent]
    #allarr=[x for x in Pent if x in Hex]
    for i in narr:
        num=i*(3*i-1)/2

    print(num)
    pass
main()
