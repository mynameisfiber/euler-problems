#!/usr/bin/python
"""
Consider the number 45656. 
It can be seen that each pair of consecutive digits of 45656 has a difference of one.
A number for which every pair of consecutive digits has a difference of one is called a step number.
A pandigital number contains every decimal digit from 0 to 9 at least once.
How many pandigital step numbers less than 1040 are there?
"""

from progressbar import ProgressBar


def pandigital(n):
    nums = set(n)
    return len(nums) == 10


def stepNumber(n):
    for i in range(len(n)-1):
        if abs(n[i]-n[i+1]) != 1:
            return i+1
    return 0


def list_num_add(cur, add, idx=-1, max=9):
    cur[idx] += add
    i = len(cur)-1
    while cur[i] > max:
        diff = cur[i] - max
        cur[i] = 0
        if i == 0:
            return [diff, ] + cur
        cur[i-1] += diff
        i -= 1
    return cur


def generate_step_number(state=[0,]):
    while 1:
        for cur_num in range(1,10):
            num = [cur_num, ]
            max_n = 0
            min_n = 9
            for i in state:
                new_num = num[-1] + 2*i - 1
                max_n = max(max_n, new_num)
                min_n = min(min_n, new_num)
                num.append(new_num)
                if not 0 <= new_num < 10:
                    num = False
                    break
            if num and min_n == 0 and max_n == 9:
                yield num
        state = list_num_add(state, 1, max=1)


if __name__ == "__main__":
    assert( stepNumber([int(x) for x in "121"])        == 0           )
    assert( stepNumber([int(x) for x in "111"])        == 1           )
    assert( pandigital([int(x) for x in "1234567890"]) == True        )
    assert( pandigital([int(x) for x in "1"])          == False       )
    assert( list_num_add([9, ], 1)                     == [1, 0]      )

    count = 0
    start_state = [int(x) for x in "000000000" ]
    progress = ProgressBar(maxval=40).start()
    for num in generate_step_number(start_state):
        progress.update(len(num))
        if len(num) >= 40:
            break
        count += 1

    print "Total number found: ", count
