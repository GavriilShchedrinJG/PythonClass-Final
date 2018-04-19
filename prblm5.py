def main():
    ## only need to care about the primes 2,3,5,7,11,13,17,19
    ## lcm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
    ## = lcm(lcm(1,2),3..) Remove any number that is a multiple of 2 numbers previously listed
    ## = -> lcm(2,3,4,5,7,9,11,12,13,15,16,17,19,20)
    ## = -> lcm(2,3,2*2,5,7,3*3,11,2*2*3,5*3,2*2*2*2,19,2*2*5)
    ## = -> lcm(2^4,3^2,5,7,11,13,17,19)
    print((2**2)**2*(3**2)*5*7*11*13*17*19)
    return;
main()
