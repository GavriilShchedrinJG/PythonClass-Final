def factorial(x):
    if x ==0:
        return 1
    y=1
    for i in range(x,1,-1):
        y*=i
    return(y)

def main():
    ans=[]
    for i in range(144,1000000):
        #i=145
        tot=0
        for j in str(i):
            tot+=factorial(int(j))
        if tot==i:
            ans.append(i)
    print(ans)
    return
main()
