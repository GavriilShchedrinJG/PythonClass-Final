import csv

def triangle(x):
    arr=[]
    for i in range(0,x):
        arr.append(int(0.5*i*(i+1)))
    return arr

def main():
    x=20
    tot=0
    nums=[]
    lst=triangle(x)
    with open('p042_words.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        data_read = [row for row in reader]
        data=data_read[0]
        #data=["S","k","y","SKY"]
        for word in data:
            wordL=word.lower()
            sumw=0
            for i in wordL:
                sumw+=(ord(i)-96)
                print(sumw)
            #print [ord(char) - 96 for char in word.lower()]
            nums.append(sumw)
    print(nums)
    for num in nums:
        if num in lst:
            tot+=1
    print(tot)
    return
main()
