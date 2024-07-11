#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   2915_和为目标值的最长子序列的长度.py
@Time    :   2024/04/05 15:17:08
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def lengthOfLongestSubsequence(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] + [float("-inf")] * target
        s = 0
        for x in nums:
            s = min(s+x,target)
            for j in range(s, x-1, -1):
                dp[j] = max(dp[j], dp[j-x]+1)
        return dp[-1] if dp[-1]>0 else -1


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    target = 9
    s = Solution()
    print(s.lengthOfLongestSubsequence(nums, target))

