import numpy as np


#really inefficient but yolo

p=1000 #max perimeter
arr=[[i,0] for i in range(0,1001)] #create and array to store values of perimeter and number of pythagorean triplets
#print(arr)
#print(arr[523][1])1
for c in range(0,p): #pick value for c
    for b in range(0,p-c): #pick value for b
        a=np.sqrt(c**2-b**2) # a is defined by these
        if (a).is_integer(): # if pythagorean triplet
            per = int(c+b+a) #calc perimeter
            if per <=1000: # if less than 1000
                arr[per][1]=arr[per][1]+1 # add one to the counter array

maxn=0 #this loop finds the max number of triplets
for i in range(0,len(arr)):
    if arr[i][1]>maxn:
        maxn=arr[i][1]

#this loop just prints the array element that has the max number of triplets
for i in range(0,len(arr)):
    if arr[i][1]==18:
        print(arr[i])

print (maxn)
#print(arr)
#print(np.amax(arr,axis=1))
