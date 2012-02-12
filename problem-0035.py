#!/usr/local/python

def primes(n):
	""" returns a list of prime numbers from 2 to < n """
	if n < 2: return []
	if n == 2: return [2]
	s = range(3, n, 2)
	mroot = n ** 0.5
	half = len(s)
	i = 0
	m = 3
	while m <= mroot:
		if s[i]:
			j = (m * m - 3)//2
			s[j] = 0
			while j < half:
				s[j] = 0
				j += m
		i = i + 1
		m = 2 * i + 3
	result = {2:True}
	result.update({x:True for x in s if x})
	return result

def is_circular(n,primes):
	n = str(n)
	print n
	for i in range(len(n)):
		if int(n[i:] + n[:i]) not in primes:
			return False
	return True

def rotations(i):
	rotate = i[1:] + i[0]
	while i != rotate:
		yield rotate
		rotate = rotate[1:] + rotate[0]

primes = primes(1000000)
number=0
counter = 0
for i in primes.keys():
	i = str(i)
	circular = 1
	for rot in rotations(i):
		if not primes.has_key(int(rot)):
			circular = 0
			break	
	number += circular
	counter+=1
print number
print counter
