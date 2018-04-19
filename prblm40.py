
strg=""
for i in range(1,1000000):
    strg=strg+str(i)
#print(strg)
#print(strg[10-1])
print(int(strg[0])*int(strg[10-1])*int(strg[100-1])*int(strg[1000-1])*int(strg[10000-1])*int(strg[100000-1])*int(strg[1000000-1]))
