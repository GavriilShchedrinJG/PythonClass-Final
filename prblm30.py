import numpy as np


some1=0
for x in range(10,1000000):
    some=0
    for i in str(x):
        some=int(i)**5+some
    #print(some)
    if str(some)==str(x):
        some1=+some+some1
        print(some)
        print("yay")
print(some1)
