#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :260_只出现一次的数字3.py
# @Time      :2024/07/24 10:51:36
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/single-number-iii/
from typing import List

def singleNumber(self, nums: List[int]) -> List[int]:
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    cls = xor_sum & (-xor_sum)
    #   cls = xor_sum - (xor_sum & (xor_sum-1))
    x1 = x2 = 0
    for num in nums:
        if num & cls:
            x1 ^= num
        else:
            x2 ^= num

    return [x1, x2]