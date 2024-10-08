#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :15_三数之和.py
# @Time      :2024/07/29 19:16:38
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/3sum/
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            x = nums[i]
            if i>0 and x == nums[i-1]:continue
            l = i+1
            r = n-1
            while l < r:
                l_num = nums[l]
                r_num = nums[r]
                su = x+l_num+r_num
                if su > 0 :
                    r-=1
                elif su < 0:
                    l+=1
                else:
                    res.append([x,l_num,r_num])
                    r-=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                       
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res





if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))