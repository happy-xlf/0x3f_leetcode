#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   33_搜索旋转排序数组.py
@Time    :   2024/03/25 14:12:27
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
class Solution(object):
    def check(self, nums, mid, target, end_num):
        if nums[mid] > end_num and target > end_num and target <= nums[mid]:
            return True
        if nums[mid] < end_num and target <= nums[mid]:
            return True
        if nums[mid] < end_num and target > end_num:
            return True
        return False
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = -1
        r = len(nums) - 1
        end_num = nums[r]
        while l + 1 < r:
            mid = (l + r) // 2
            if self.check(nums, mid, target, end_num):
                r = mid
            else:
                l = mid
        if nums[r] == target:
            return r
        else:
            return -1

if __name__ == '__main__':
    nums = [int(k) for k in input().split(",")]
    target = int(input())
    s = Solution()
    print(s.search(nums, target))

