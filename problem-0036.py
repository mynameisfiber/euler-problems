#!/usr/local/python

from math import *

def is_palindromic(n):
	n = str(n)
	if n == n[::-1]:
		return True
	return False

 
def Denary2Binary(n):
	'''convert denary integer n to binary string bStr'''
	bStr = ''
	if n < 0:  raise ValueError, "must be a positive integer"
	if n == 0: return '0'
	while n > 0:
       		bStr = str(n % 2) + bStr
        	n = n >> 1
    	return bStr


sum=0
for i in range(1000000):
	if is_palindromic(i) and is_palindromic(Denary2Binary(i)):
		print i
		sum+=i
print sum