#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   53_最大子数组和_2.py
@Time    :   2024/10/10 20:14:22
@Author  :   Lifeng Xu 
@desc :   
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i],dp[i-1]+nums[i])
        return max(dp)
    


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray(nums))


