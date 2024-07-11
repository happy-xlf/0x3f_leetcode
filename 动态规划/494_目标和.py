#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   494_目标和.py
@Time    :   2024/04/02 10:55:46
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        target += sum(nums)
        if target%2 or target<0:
            return 0
        target = target//2
        n = len(nums)

        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i,x in enumerate(nums):
            for j in range(target+1):
                if j<x:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j] + dp[i][j-x]
        return dp[n][target]
    
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        target += sum(nums)
        if target%2 or target<0:
            return 0
        target = target//2
        n = len(nums)

        dp = [0]*(target+1)
        dp[0] = 1
        for x in nums:
            for j in range(target, x-1, -1):
               dp[j] = dp[j] + dp[j-x]
        return dp[target]
    
    def findTargetSumWays2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        target += sum(nums)
        if target%2 or target<0:
            return 0
        target = target//2
        n = len(nums)

        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0]=1
        for i,x in enumerate(nums):
            for j in range(target+1):
                if j<x:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j] + dp[i][j-x]
        return dp[n][target]    
    
if __name__ == '__main__':
    nums = [1,1,1,1,1]
    target = 3
    s = Solution()
    print(s.findTargetSumWays2(nums,target))

