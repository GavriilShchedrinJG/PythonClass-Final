def pentlist(init,end):
    arr=[]
    for i in range(init,end):
        arr.append((i*(3*i-1))/2)
    return arr

## I just moved the range untill i got an answer through brute force not fance but it gives you the answer
def main():
    init=1000
    end=3000
    lst=pentlist(init,end)
    for i in range(0,len(lst)):
        #print(i)
        for j in range(0,i):
            S=lst[i]+lst[j]
            D=lst[i]-lst[j]
            if S in lst and D in lst and j!=0:
                print(i,j,S,D)
                break
    return
main()
