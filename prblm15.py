#sounds like a combinatorics problem
#2x2 has 6 solutions were the number of downs and rights are equal order doesn't matter
#Need 2 N steps
#should just be (2*N N)

from scipy.special import binom

print(binom(40,20))
