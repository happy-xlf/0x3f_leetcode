#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gcd.py
# @Time      :2024/08/19 10:43:02
# @Author    :Lifeng
# @Description :


def gcd_self(a, b):
    if b == 0:
        return a
    else:
        return gcd_self(b, a % b)


print(gcd_self(12, 18))