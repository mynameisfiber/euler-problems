#!/usr/local/python

number = 100

factorial = 1
for i in range(1,number+1):
	factorial *= i

sum = 0
for i in str(factorial):
	sum+=int(i)

print sum