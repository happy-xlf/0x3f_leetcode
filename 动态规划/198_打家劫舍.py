#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   198_打家劫舍.py
@Time    :   2024/04/02 10:56:38
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        dp = [-1] * (len(nums))
        dp[0]=nums[0]
        if len(nums) == 1:
            return dp[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
