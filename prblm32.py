import numpy as np


totalsum=0
already=[]
for i in range(4,100):
    for ii in range(100,10000//i):
        prod=i*ii
        if prod<=9876:
            string=str(prod)+str(i)+str(ii)
            if len(string)==9 and not '1234567890'[:9].strip(string):
                if prod not in already:
                    already.append(prod)
                    totalsum=totalsum+prod

print(totalsum)

            #check for all digits
