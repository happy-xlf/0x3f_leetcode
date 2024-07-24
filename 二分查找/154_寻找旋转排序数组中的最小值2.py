#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :154_寻找旋转排序数组中的最小值2.py
# @Time      :2024/07/24 11:03:38
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/description/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[l]


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3,5,1]))



