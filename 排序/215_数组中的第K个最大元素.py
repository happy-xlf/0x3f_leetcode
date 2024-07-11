#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   215_数组中的第K个最大元素.py
@Time    :   2024/04/02 14:43:20
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    # [3,2,1,5,6,4], k = 2
    def quick_sort(self, nums,l,r):
        value = nums[l]
        while l<r:
            while l<r and nums[r]<=value:
                r-=1
            nums[l] = nums[r]
            while l<r and nums[l]>=value:
                l+=1
            nums[r] = nums[l]
        nums[l] = value
        return l

    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # [3,2,1,5,6,4], k = 2
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = self.quick_sort(nums,l,r)
            if mid == k-1:
                return nums[mid]
            elif mid > k-1:
                r = mid-1
            else:
                l = mid+1

if __name__ == '__main__':
    s = Solution()
    nums = [1]
    k = 1
    print(s.findKthLargest(nums,k))


