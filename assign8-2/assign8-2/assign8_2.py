#! /usr/bin/env python3
#coding:utf-8

import re

def rm_html_markup(s):
    return re.sub(r'<.+?>','',s)

    
def reg_test():
    assert rm_html_markup('<a href=”index.htm”>Welcome to Fudan University!</a>') == 'Welcome to Fudan University!'
    print('Self test passed!')


def main():
    s = input('Please input a string with HTML markup:')
    print(rm_html_markup(s))


if __name__ == '__main__':
    reg_test()
    main()
