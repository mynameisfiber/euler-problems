#!/usr/bin/python
"""
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
 9   8   7   6  5   4  3  2  1  0
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def add_chain(num, chain):
    orig_num = num
    length = 0
    temp_chain = {}
    while num not in chain:
        num = num / 2.0 if num%2==0 else 3.0*num+1.0
        length += 1
        temp_chain[num] = length
    base_length = chain[num]
    chain.update({k:length+base_length-v for k,v in temp_chain.iteritems()})
    return length+base_length

if __name__ == "__main__":
    from progressbar import ProgressBar
    chain = {1:1}
    assert( add_chain(5, chain) == 6 )
    
    max_chain_length = 1
    max_chain_number = 1
    progress = ProgressBar(maxval=100000000).start()
    for i in xrange(1,100000000):
        tmp_length = add_chain(i, chain)
        if max_chain_length < tmp_length:
            max_chain_length = tmp_length
            max_chain_number = i
        progress.update(i)
    print "Maximum chain length: %d"%max_chain_length
    print "Maximum chain number: %d"%max_chain_number
