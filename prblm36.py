import numpy as np



#Function that checks if input is a palindrome
def pal(x):
    x=str(x)
    word=x.lower()
    if word == word[::-1]:
        return True
    else:
        return False
    return;


def main():
    pal10=[i for i in range(0,10**6) if pal(i)] #find palindromes under a million
    tmp=[bin(x)[2:] for x in pal10] #covert to binary
    palbin=[x for x in tmp if pal(x)] #find binary palindromes
    palbin=[int(x,2) for x in palbin] #convert back to base 10
    print (palbin)
    print(np.sum(palbin)) #sums them
    return;

main()
