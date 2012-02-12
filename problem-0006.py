#!/usr/local/python

"""Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

sumSquares, sum = reduce(lambda x, y : [x[0]+y*y, x[1]+y], range(1,101), [0,0])
print sum*sum - sumSquares
