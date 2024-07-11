#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   76_数组中的第K个最大元素.py
@Time    :   2024/03/27 18:17:19
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
"""


class Solution(object):
    # 找出第几大
    # def sort_k(self, num, l, r):
    #     value = num[l]
    #     while l < r:
    #         while l < r and num[r] <= value:
    #             r -= 1
    #         num[l] = num[r]
    #         while l < r and num[l] >= value:
    #             l += 1
    #         num[r] = num[l]
    #     num[l] = value
    #     return l

    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     l = 0
    #     r = len(nums) - 1
    #     while True:
    #         idx = self.sort_k(nums, l, r)
    #         if idx == k - 1:
    #             return nums[idx]
    #         elif idx < k - 1:
    #             l = idx + 1
    #         else:
    #             r = idx - 1

    def sort_k(self, num, l, r):
        value = num[l]
        while l < r:
            while l < r and num[r] >= value:
                r -= 1
            num[l] = num[r]
            while l < r and num[l] <= value:
                l += 1
            num[r] = num[l]
        num[l] = value
        return l

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while True:
            idx = self.sort_k(nums, l, r)
            if idx == len(nums) - k:
                return nums[idx]
            elif idx < len(nums) - k:
                l = idx + 1
            else:
                r = idx - 1


if __name__ == "__main__":
    s = Solution()
    # nums = [int(k) for k in input().split()]
    nums = [2, 4, 6, 8, 1, 3, 5, 7]
    print(s.findKthLargest(nums, 3))
