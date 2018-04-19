def mults(x):
    limit=x-1
    num3s=int(limit/3)
    num5s=int(limit/5)
    numdoubles=int(limit/15)
    sum_of_threes=0
    sum_of_fives=0
    doubles=0
    for i in range(1,num3s+1):
        sum_of_threes=3*i+sum_of_threes
    for i in range(1,num5s+1):
        sum_of_fives=5*i+sum_of_fives
    for i in range(1,numdoubles+1):
        doubles=3*5*i+doubles

    print(sum_of_fives+sum_of_threes-doubles)
#####################################################

    mults3=0
    mults5=0
    num=3
    while (num<x):
        mults3=num+mults3
        num=num+3
    num=5
    while (num<x):
        if (num%3==0):
            num=num+5
        mults5=num+mults5
        num=num+5
    print(mults3+mults5)

    return;

def main():
    print("hello")
    mults(1000)
    return;

main()
