#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :33_搜索旋转排序数组.py
# @Time      :2024/07/29 14:44:42
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/search-in-rotated-sorted-array/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 左侧为有序数组
            if nums[mid] > nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            # 右侧为有序数组
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return l if nums[l] == target else -1



if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))