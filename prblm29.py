lst=[]

for i in range(2,101):
    for j in range(2,101):
        sol=i**j
        if sol not in lst:
            lst.append(sol)
print(len(lst))
