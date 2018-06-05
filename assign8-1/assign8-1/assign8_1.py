#! /usr/bin/env python3
#coding:utf-8

import re

def email_valid_check(addr):
    if re.match(r'^\w+(\.\w+)*@\w+(\.\w+)*\.[a-zA-Z]+$',addr):
        return True
    else:
        return False

def email_regexp_test():
    assert email_valid_check('jkhe17@fudan.edu.cn')
    assert email_valid_check('jkhe17@fudanedu.cn')
    assert email_valid_check('jkhe17@fudan_edu.com')
    assert email_valid_check('jk.he17@fudan.edu.com')
    assert not email_valid_check('jkhe17&fudan.edu.cn')
    assert not email_valid_check('jkhe17@fudaneducn')
    print('Self test passed!')


def main():
    email=input('Please input an email address:')
    if email_valid_check(email) == True:
        print('Is "%s" a valid email address? Ture'%email)
    else:
        print('Is "%s" a valid email address? False'%email)


if __name__ == '__main__':
    email_regexp_test()
    main()
