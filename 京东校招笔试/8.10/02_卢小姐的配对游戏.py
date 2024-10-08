#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :02_卢小姐的配对游戏.py
# @Time      :2024/08/16 23:16:53
# @Author    :Lifeng
# @Description :
import sys
from collections import Counter
n,x = map(int, input().split())
nums = list(map(int, input().split()))

# dt = {}
# for it in nums:
#     dt[it] = dt.get(it, 0) + 1
dt = Counter(nums)

res = 0
used = []
for k, v in dt.items():
    if x - k != k and k not in used and x-k not in used:
        other_value = dt[x-k]
        res += v * other_value
        used.append(k)
        used.append(x-k)

print(res)
