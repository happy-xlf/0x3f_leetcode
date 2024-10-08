#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :34_二分第一个和最后一个.py
# @Time      :2024/08/26 17:35:57
# @Author    :Lifeng
# @Description :
from typing import List

class Solution:
    def binaryLeft(self, nums: List[int], target: int) -> int:
        l,r = -1, len(nums)
        while l +1 != r:
            mid = l+(r-l)//2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return r
    
    def binaryRight(self, nums: List[int], target: int) -> int:
        l,r = -1, len(nums)
        while l +1!= r:
            mid = l+(r-l)//2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        return l


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        left = self.binaryLeft(nums, target)
        right = self.binaryRight(nums, target)
        if left<=right and right < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        else:
            return [-1, -1]
        

if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([8,8], 9))

