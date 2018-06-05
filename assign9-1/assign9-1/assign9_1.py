#!  /usr/bin/env python3
#coding:utf-8

def isLeap(year):
    '''Check if a year is leap year.'''
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


assert isLeap(2000) == True
assert isLeap(2004) == True
assert isLeap(2001) == False
assert isLeap(2100) == False
