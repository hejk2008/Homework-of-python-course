#! /usr/bin/env python3
# coding: utf-8

def main():
    with open('sample1.txt','r') as f:
        content = f.read()
    content = content.upper()
    with open('sample2.txt','w') as f:
        f.write(content)

if __name__ =='__main__':
    main()
