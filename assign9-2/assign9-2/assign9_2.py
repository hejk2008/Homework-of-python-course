#! /usr/bin/env python3
#coding:utf-8

def f1(s):
    '''Transform a string to palindrome.'''
    return s+s[-2::-1]


def f2(s):
    '''Check if a string is palindrome.'''
    return s == s[::-1]


assert f1('asddf') == 'asddfddsa'
assert f1('a') == 'a'
assert f2('asddf') == False
assert f2('asddfddsa') == True
