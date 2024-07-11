#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   912_排序数组.py
@Time    :   2024/05/18 17:01:57
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums, left, right):
            if left>=right:
                return nums
            l = left
            r = right
            t = nums[l]
            while l<r:
                while l<r and nums[r]>=t:
                    r-=1
                nums[l] = nums[r]

                while l<r and nums[l]<=t:
                    l+=1
                nums[r] = nums[l]
            
            nums[l] = t
            quick_sort(nums,left,l-1)
            quick_sort(nums,l+1, right)
            return nums
        
        nums = quick_sort(nums,0,len(nums)-1)
        return nums
    

def quick_sort(nums, left, right):
    if left>=right:
        return nums
    l = left
    r = right
    t = nums[l]
    while l<r:
        while l<r and nums[r]>=t:
            r-=1
        nums[l] = nums[r]

        while l<r and nums[l]<=t:
            l+=1
        nums[r] = nums[l]
    
    nums[l] = t
    quick_sort(nums,left,l-1)
    quick_sort(nums,l+1, right)
    return nums

if __name__ == '__main__':
    nums = [5,2,3,1]
    # nums = quick_sort(nums,0,3)
    # print(nums)
    s = Solution()
    print(s.sortArray(nums))
