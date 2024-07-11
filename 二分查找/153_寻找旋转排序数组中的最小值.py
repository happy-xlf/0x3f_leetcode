#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   153_寻找旋转排序数组中的最小值.py
@Time    :   2024/03/25 11:29:48
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''


class Solution(object):
    # def check(self, mid, end_num):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [3,4,5,1,2]
        #  1
        l = -1
        r = len(nums)-1
        end_num = nums[r]
        while l+1<r:
            mid = (l+r)//2
            if nums[mid] > end_num:
                l = mid
            else:
                r = mid
        return nums[r]




if __name__ == '__main__':
    nums = [int(k) for k in input().split(",")]
    s = Solution()
    print(s.findMin(nums))
