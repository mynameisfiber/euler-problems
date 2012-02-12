#!/usr/local/python

x1 = 1
x2 = 1

index=2
while len(str(x2)) <> 1000:
	x1, x2 = x2, x1+x2
	index+=1
print index