#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   三数之和.py
@Time    :   2024/04/02 15:55:47
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            x = nums[i]
            if x+nums[i+1]+nums[i+2]>0:
                break
            if x+nums[-1]+nums[-2]<0:
                continue
            l = i+1
            r = n-1
            while l<r:
                x_sum = x+nums[l]+nums[r]
                if x_sum == 0:
                    res.append([x,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    r-=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif x_sum < 0:
                    l+=1
                else:
                    r-=1
        return res



if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    print(s.threeSum(nums))

