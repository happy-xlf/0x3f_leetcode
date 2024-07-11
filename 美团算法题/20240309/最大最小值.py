#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   最大最小值.py
@Time    :   2024/03/30 09:54:31
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

def maxmin_def(l, r, a):
    cnt = 0
    sum = 0 
    for it in a:
        if it!=0:
            sum+=it
        else:
            cnt+=1
    return sum+l*cnt, sum+r*cnt 


if __name__ == '__main__':
    n, q =map(int, input().split())
    a = [int(k) for k in input().split()]
    while q:
        q -= 1
        l, r = map(int, input().split())
        print(maxmin_def(l,r,a))
