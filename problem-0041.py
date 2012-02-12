#!/usr/local/python

def find_primes(n):
        if n==2: return [2]
        elif n<2: return []
        s=range(3,n+1,2)
        mroot = n ** 0.5
        half=(n+1)/2-1
        i=0
        m=3
        while m <= mroot:
                if s[i]:
                        j=(m*m-3)/2
                        s[j]=0
                        while j<half:
                                s[j]=0
                                j+=m
                i=i+1
                m=2*i+3
        return [2]+[x for x in s if x]

def pandigital(n):
	n = str(n)
	for i in range(1,len(n)+1):
		if str(i) not in n:
			return 0
	print n
	return i

print "Finding primes"
primes = find_primes(987654321)
number = 0

print "Finding pandigital's"
for i in primes:
	if pandigital(i) and i > number:
		number = i

print number