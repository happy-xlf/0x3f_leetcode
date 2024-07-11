#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   53_最大子数组和.py
@Time    :   2024/05/18 17:45:37
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0] for _ in range(len(nums))]
  
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
     

        return max(dp)

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray(nums))

        