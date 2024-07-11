#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   删除区间.py
@Time    :   2024/03/30 11:17:05
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

def del_sum(a, k):
    a2 = [0] * len(a)
    a5 = [0] * len(a)
    for i in range(len(a)):
        while  a[i]%2 == 0:
            a[i] = a[i] // 2
            a2[i] += 1
        while  a[i]%5 == 0:
            a[i] = a[i] // 5
            a5[i] += 1
    cnt2 = sum(a2)
    cnt5 = sum(a5)
    l = 0
    res = 0
    for r in range(len(a)):
        cnt2 = cnt2 - a2[r]
        cnt5 = cnt5 - a5[r]
        while l <= r and min(cnt2, cnt5) < k:
            cnt2 = cnt2 + a2[l]
            cnt5 = cnt5 + a5[l]
            l+=1
        res+= r-l+1
    return res

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [int(k) for k in input().split()]
    print(del_sum(a,k))
