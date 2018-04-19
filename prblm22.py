import csv

 zvbd    arr=[]n cg
    for i in range(0,x):
        arr.append(int(0.5*i*(i+1)))
    return arr

def main():
    x=20
    tot=0
    names=1
    nums=[]#keeps the scores
    #lst=triangle(x)
    with open('p022_names.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        data_read = [row for row in reader]
        data=data_read[0]
        #data=["S","k","y","SKY"]
        #data=["colin"]
        data=sorted(data)
        for word in data:
            wordL=word.lower()
            sumw=0
            for i in wordL:
                sumw+=(ord(i)-96)

                #print(sumw)
            #print [ord(char) - 96 for char in word.lower()]
            score=sumw*names
            nums.append(score)
            names+=1
    # print(nums)
    # for num in nums:
    #     if num in lst:
    #         tot+=1
    print(nums[937]/938,nums[938]/939)
    print(sum(nums))
    return
main()
