#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :05_最大最小连续子序列和.py
# @Time      :2024/08/17 21:02:20
# @Author    :Lifeng
# @Description :
import sys

n,k = map(int, input().split())
a_list = list(map(int, input().split()))

def nums_max(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    maxn =0
    l,r = 0,0
    temp_l =0
    temp_r =0
    for i in range(1, len(nums)):
        if nums[i] > dp[i-1] + nums[i]:
            temp_l = i
            temp_r = i
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1] + nums[i]
            temp_r = i

        if dp[i] > maxn:
            maxn = dp[i]
            l = temp_l
            r = temp_r

    return maxn, l, r

def nums_min(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    minn =100000000
    l,r = 0,0
    temp_l =0
    temp_r =0
    for i in range(1, len(nums)):
        if nums[i] < dp[i-1] + nums[i]:
            temp_l = i
            temp_r = i
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1] + nums[i]
            temp_r = i

        if dp[i] < minn:
            minn = dp[i]
            l = temp_l
            r = temp_r

    return minn, l, r


max_sum, max_l, max_r = nums_max(a_list)
print(max_l, max_r, max_sum)
for i in range(max_l, max_r+1):
    a_list[i] = a_list[i] * k
print("list: ", a_list)
min_sum, min_l, min_r = nums_min(a_list)
print(min_l, min_r, min_sum)
for i in range(min_l, min_r+1):
    a_list[i] = a_list[i] * k
print("list: ", a_list)
print(sum(a_list))