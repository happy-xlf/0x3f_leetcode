#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   01矩阵.py
@Time    :   2024/03/30 15:57:19
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

def o1(a):
    n = len(a)
    m = len(a[0])
    res = 0
    for i in range(n-1):
        for j in range(m-1):
            if a[i][j]+a[i+1][j]+a[i][j+1]+a[i+1][j+1] == 2:
                res += 1
    print(res)
    return res


if __name__ == '__main__':
    n, m=map(int, input().split())
    ju = []
    for _ in range(n):
        s = [int(k) for k in input()]
        ju.append(s)
    o1(ju)
