def check(x,y):
    print(x,y)
    if x%y==0:
        return True
    else:
        return False
def main():
    y=[2,3,5,7,11,13,17]
    ans=[]
    count=0
    #d6 has to be 0 or 5
    d6=[0,5]
    #d6d7d8 has to be divisable by 11 and start with 5
    d6d7d8=[]
    for i in range(500,599):
        if i%11==0:
            if len(set(str(i)))==3:
                d6d7d8.append(i)
    print(d6d7d8)
    #d7d8d9 must be divisible by 13 not contain 5 and be unique
    d7d8d9=[]
    for num in d6d7d8:
        pos=abs(num) % 100
        fill=pos*10
        for i in range(0,10):
            if (fill+i)%13==0:
                str789=str(fill+i)
                if len(str789)==3:
                    if not '5' in set(str789):
                        if len(set(str789))==3:
                            d7d8d9.append(fill+i)
    print(d7d8d9)
    #similarly
    d8d9d0=[]
    for num in d7d8d9:
        pos=abs(num) % 100
        fill=pos*10
        for i in range(0,10):
            if (fill+i)%17==0:
                str890=str(fill+i)
                if len(str890)==3:
                    if not '5' in set(str890):
                        if len(set(str890))==3:
                            d8d9d0.append(fill+i)
    print(d8d9d0)
    #similarly
    d5d6d7=[]
    for num in d7d8d9:
        pos=int(str(num)[0])
        #print(pos)
        for i in range(1,10):
            #print(pos+i*100)
            if (pos+50+i*100)%7==0:
                str567=str(pos+50+i*100)
                if len(str567)==3:
                    if not '6' in set(str567):
                        if len(set(str567))==3:
                            d5d6d7.append(pos+50+i*100)
    print(d5d6d7)
    lastsix=[]
    for num in d5d6d7:
        for num2 in d8d9d0:
            test=num*1000+num2
            if len(set(str(test)))==6:
                lastsix.append(test)
    print(lastsix)
    d3d4d5=[]
    for i in range(10,1000):
        if i%3==0:
            if not('5' in set(str(i)) or '2' in set(str(i)) or '7' in set(str(i)) or '8' in set(str(i)) ):
                if int(str(i)[-1])==3 or int(str(i)[-1])==9:
                    if int(str(i)[-2])%2==(0):
                        if len(str(i))>2:
                            if len(set(str(i)))==3:
                                if int(str(i)[0])!=(9):
                                    if not('6' in str(i) and '9' in str(i)):
                                        d3d4d5.append(i)
                        else:
                            if not('6' in str(i) and '9' in str(i)):
                                d3d4d5.append(i)
    print("d3d4d5: ",d3d4d5)
    d2d3d4=[]
    # these force dqd2 to either 14 or 41
    d1d2=[14,41]
    last8=[]
    for num in d3d4d5:
        for num2 in lastsix:
            if int(str(num)[-1])== int(str(num2)[0]):
                last8.append((num-int(str(num)[-1]))*100000+num2)
    print(last8)
    fin=[]
    for num in d1d2:
        for num2 in last8:
            fina=num*100000000+num2
            if len(set(str(fina)))==10:
                fin.append(fina)
    # #     x=1234567890
    #     drool=True
    #     for div in y:
    #         #print(div)
    #         if not check(num,div):
    #             drool=False
    #     if drool:
    #         ans.append(x)
    #     count+=1
    print(fin)
    print("sum: ", sum(fin))
    return
main()
