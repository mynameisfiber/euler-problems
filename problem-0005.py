#!/bin/local/python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

max_num = reduce(lambda x,y : x*y, range(1,21))
test= 0
found=1
while found != 0 and test < max_num:
	test += 2520
	found = 0
	for i in range(10,21):
		found += test % i
		
print test
