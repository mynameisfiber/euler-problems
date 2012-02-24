#!/usr/local/bin/python
"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime

num_first_sunday = 0
for year in xrange(1901, 2001):
    for month in xrange(1,13):
        test_date = datetime.datetime(year, month, 1)
        if test_date.strftime("%u") == "7":
            num_first_sunday += 1
print "Number of sundays landing on the first of the month: %d"%num_first_sunday
