#!/usr/bin/python
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n):
    divisors = []
    for i in xrange(1,n):
        if n%i == 0:
            divisors.append(i)
    return sum(divisors)

if __name__ == "__main__":
    n_to_sum = {}
    amicable_sum = 0
    for i in xrange(1, 10000):
        n_to_sum[i] = d(i)
        if n_to_sum[i] in n_to_sum and n_to_sum[n_to_sum[i]] == i and n_to_sum[i] != i:
            amicable_sum += i + n_to_sum[i] 

    print "Sum: %d"%amicable_sum
