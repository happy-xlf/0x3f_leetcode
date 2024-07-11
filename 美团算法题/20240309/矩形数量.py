#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   矩形数量.py
@Time    :   2024/03/30 10:23:20
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
def query(x1,y1,x2,y2,s):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]


def ju_sum(s):
    for length in range(1,len(s)):
        res = 0
        if length == 1:
            print(res)
            continue
        for st in range(1,len(s)-length+1):
            for ed in range(1,len(s)-length+1):
                ans = query(st,ed,st+length-1,ed+length-1,s)
                if ans*2 == length**2:
                    res+=1
        print(res)

if __name__ == '__main__':
    n = int(input())
    s = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1,n+1):
        t = [int(i) for i in input()]
        for j in range(1,n+1):
            s[i][j] = t[j-1]
    print(s)
    #前缀合
    for i in range(1,n+1):
        for j in range(1,n+1):
            s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + s[i][j]
    print(s)
    ju_sum(s)
