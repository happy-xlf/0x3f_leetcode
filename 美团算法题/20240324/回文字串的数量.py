#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   回文字串的数量.py
@Time    :   2024/03/30 16:06:48
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

def check(s):
    k=""
    res = 0
    for it in s:
        if it ==k:
            res+=1
        k = it
    print(res)
    return res

if __name__ == '__main__':
    n = int(input())
    s = str(input())
    check(s)

