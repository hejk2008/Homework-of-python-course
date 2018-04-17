#! /usr/bin/env python3
# coding:utf-8

#水仙花数是一个n(n大于等于3）位数字的数，它等于每个数字的n次幂之和。
#例如,153是一个水仙花数，因为153=1**3+5**3+3**3。
#求所有3位数中的水仙花数。
#方法1：用列表推导式，将下一行补充完整。
narcissus_list = [n for n in range(100,1000) if n == (n//100)**3 + (n//10%10)**3 + (n%10)**3]
print(narcissus_list) 

#方法2：用生成器推导式，将下一行补充完整。
narcissus_gen = (n for n in range(100,1000) if n == (n//100)**3 + (n//10%10)**3 + (n%10)**3)
narcissus = [next(narcissus_gen) for x in range(4) ] 
print(narcissus) 
