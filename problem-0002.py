#!/usr/local/python
"""Find the sum of all the even-valued terms in the sequence which do not exceed four million."""

x, y = 1, 2
sum = 0
while y <= 4000000:
    if y % 2 == 0:
        sum += y
    x, y = y, x+y
print sum        
