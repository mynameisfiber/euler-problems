#!/usr/bin/python
"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Note: http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
"""

def n(m):
    return (500.0 - m*m) / (1.0*m)

def a(n,m):
    return m*m - n*n

def b(n,m):
    return 2*m*n

def c(n,m):
    return m*m + n*n

if __name__ == "__main__":
    m = 1
    while n(m) >= m or n(m)%1 > 1e-10:
        m += 1
    n = n(m)
    print "n, m = %d, %d"%(n, m)
    print "a, b, c = %d, %d, %d"%(a(n,m), b(n,m), c(n,m))
    print "a * b * c = %d"%(a(n,m)*b(n,m)*c(n,m))
