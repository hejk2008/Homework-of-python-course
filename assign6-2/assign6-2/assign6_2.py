#! /usr/bin/env python3
# coding:utf-8


def main():
    #answer = [(a, b, c) for a in range(21) for b in range(34) for c in range(101-a-b)
    #          if a*5 + b*3 +c/3 == 100 and a+b+c == 100]
    #print(answer)
    for a in range(21):
        for b in range(34):
            c = 100-a-b
            if a*5 + b*3 +c/3 == 100:
                print(a, b, c)


if __name__ == '__main__':
    main()

