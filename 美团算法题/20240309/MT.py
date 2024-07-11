#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   MT.py
@Time    :   2024/03/30 09:33:43
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

def mt(n,k,str_input):
    cnt = 0
    for it in str_input:
        if it != 'M' and it != 'T':
            cnt += 1
    res = (n-cnt) + min(cnt,k)
    return res
    

    

if __name__ == '__main__':
    n, k = map(int, input().split())
    str_input = str(input())
    print(mt(n,k,str_input))

