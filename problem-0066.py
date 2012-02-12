#!/usr/local/python
"""Find the value of D  1000 in minimal solutions of x for which the largest value of x is obtained."""
"""dedicated to nick gazel"""

import decimal

def solveDiophantine(D):
    """Solve Diophantine using Pell's technique with continued fractions"""
    """Interesting: Precession has to be the same as the number of steps taken"""
    """Note: We will assume that a solution exists to save CPU time for testing
             if last of convergents have been found"""
    decimal.getcontext().prec = 80
    v = []
    w = [(0,1), (1,0)]
    start = x = decimal.Decimal(D).sqrt()
    #print start
    count = 1
    while True:
        a = int(x) 
        v.append(a)
        n = len(v)-1
        pn = v[n]*w[n+1][0] + w[n][0]
        qn = v[n]*w[n+1][1] + w[n][1]
	#print count, a, x, pn**2 - D * qn**2
        x -= a
	w.append((pn,qn))
	
	#print pn**2 - D * qn**2, (pn,qn),abs(start - float(pn)/float(qn))
	if pn**2 - D * qn**2 == 1:
		del w
		#print D, (pn,qn)
		return pn
        #if abs(start - pn/qn) == 0: 
	#	del w
	#	return 0
        x = 1/x
	count +=1

#print solveDiophantine(991)

max=0
d=0
unsolved=0
for i in range(2,1001):
	if (i**.5)%1 > 1e-5:
		print "Testing D =", i
		test = solveDiophantine(i)
		#print test, i
		if test == 0:
			print "No Solution for", i
			unsolved+=1
		if test >= max:
			max = test
			d = i
			#print "D:",d, "Max:",max
print "unsolved =", unsolved
print "d =",d
print "max(x) =",max
