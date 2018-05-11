#! /usr/bin/env python3
# coding:utf-8

def main():
    for i in range(1,100000):
        i_str = '0'+str(i)
        for first_num_lenth in range(1,len(i_str)):
            first_num = int(i_str[:first_num_lenth])
            second_num = int(i_str[first_num_lenth:])
            if (i == (first_num + second_num) ** 2):
                print('%d=(%d+%d)**2'%(i,first_num,second_num))


if __name__ == '__main__':
    main()

