#!/usr/bin/python
"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the divisors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import numpy as np
import math

def get_primes(upto):
    """
    Sieve method for finding primes.  Implemintation taken from:
    http://rebrained.com/?p=458
    """
    primes=np.arange(3,upto+1,2)
    isprime=np.ones((upto-1)/2,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor]=0
    return np.insert(primes[isprime],0,2)


def num_divisors(n):
    primes = get_primes(int(n**0.5))
    cur_num = n
    divisors = {}
    for i in primes:
        while cur_num % i == 0:
            cur_num /= i
            divisors[i] = divisors.get(i, 0) + 1
        if cur_num == 0:
            break
    num = 1
    for i in divisors.values():
        num *= (i + 1)
    return num


def iterate_triangle_numbers():
    triangle = 0
    i = 1
    while True:
        triangle += i
        i += 1
        yield triangle

if __name__ == "__main__":
    assert( num_divisors(24) == 8 )
    n = 1
    for n in iterate_triangle_numbers():
        divisors = num_divisors(n)
        if divisors > 500:
            break
    print "n = %d has %d divisors"%(n, divisors)