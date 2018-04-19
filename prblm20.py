
def factorial(x):
    if(float(x)<1):
        print("please use a integer greater than 0")
    num=int(x)
    tot=1
    while(num>1):
        tot=tot*num
        num=num-1
    return tot;

num=factorial(100)

string=str(num)

s=0
for i in range(len(string)):
    s=s+int(string[i])
print(s)
