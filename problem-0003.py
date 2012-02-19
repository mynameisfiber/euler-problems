#!/usr/bin/python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

largest = 0
for prime in file("/Users/micha/projects/Misc-Old-Projects/numbers/prime/primes.1e9", "r").xreadlines():
    prime = int(prime.strip())
    if prime > 775147:
        break
    if 600851475143 % prime == 0:
        largest = prime
print largest
