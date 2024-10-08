#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :埃式素数晒.py
# @Time      :2024/08/19 10:35:19
# @Author    :Lifeng
# @Description :

def ai_su(n):
    dp = [True] * n
    res = []
    for i in range(2, n):
        if dp[i]:
            res.append(i)
            for j in range(i * i, n, i):
                dp[j] = False
    return res


print(ai_su(100))
