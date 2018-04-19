def pal(x):
    #print(str(x)[::-1]==str(x))
    if str(x)[::-1]==str(x):
        return True
    else:
        return False
ans=[]
for i in range(100,999):
    for j in range(100,999):
        if pal(i*j):
            ans.append(i*j)
print(max(ans))
