#!/bin/local/python
"""Find the largest palindrome made from the product of two 3-digit numbers."""

interate=range(999, 99, -1)
largest=0
for i, outer in enumerate(interate):
    for inner in interate[i:]:
        test = outer * inner
        if str(test)[::-1] == str(test):
            largest = max(largest, test)

print "Largest: ", largest
        

