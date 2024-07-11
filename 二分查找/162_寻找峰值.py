#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   162_寻找峰值.py
@Time    :   2024/03/25 11:20:19
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input:[1,2,3,1]
        # output: 2
        l = -1
        r = len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid
            else:
                r = mid
        return r


if __name__ == '__main__':
    nums  = [int(k) for k in input().split(",")]
    s = Solution()
    print(s.findPeakElement(nums))
