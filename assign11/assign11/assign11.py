#! /usr/bin/env python3
# coding: utf-8

def main():
    try:
        f1 = open('sample1.txt','r')
    except FileNotFoundError:
        print("No such file or directory: 'sample1.txt'")
        return None
    try:
        content = f1.read()
    except UnicodeDecodeError:
        print('File codec error, please save the file in UTF-8.')
        return None
    finally:
        f1.close
    content = content.upper()
    try:
        f2 = open('sample2.txt','w')
    except PermissionError:
        print('Permission error, please set the correct premission manually.')
        return None
    else:
        f2.write(content)
        f2.close


if __name__ =='__main__':
    main()
