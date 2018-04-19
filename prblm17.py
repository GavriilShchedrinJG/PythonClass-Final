dic={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,1000:8}
tot=0

##### my version was buggy and the divmod stuff i found on SE fixed a fair amount
def length(x):
    if x<=20:
        return dic[x]
    elif x<100:
        tens,ones=divmod(x,10)
        #print(tens)
        return dic[tens*10]+dic[ones]
    elif x<1000:
        hundreds, rest = divmod(x, 100)
        fix=0
        if rest==0:fix=3
        return length(hundreds)+len("hundred")+3+length(rest)-fix
    else:
        thousands,rest=divmod(x,1000)
        return length(thousands)+8+length(rest)

print(sum([length(x) for x in range(1,1001)]))
