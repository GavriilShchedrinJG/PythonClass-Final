
def div(x):
    tot=0
    i=2
    upper=x
    while i<upper:
        if x%i==0:
            upper=x/i
            tot+=upper
            if upper !=i:tot+=i
        i+=1
        if tot>x:
            return True
    return False

ans=[]

# for i in range(0,28123):
#######3brute force code I wrote that is really slow####3
# i=12
# print(div(12))
# sums=0
# abun=[x for x in range(11,28123) if div(x)]
#
# for i in range(12,28123):
#     for bun in abun:
#         if bun >=i and div(i+bun):
#             sums+=i
#
# print(sums)

#better solution from Stack exchange


abun=[x for x in range(11,28123) if div(x)]
dbun={x:x for x in abun}

sums=1
for i in range(2,28123):
    boo=True
    for k in abun:
        if k<i:
            if(i-k) in dbun:
                boo=False
                break
        else:break
    if boo: sums+=i
print(sums)
