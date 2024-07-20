#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :503_下一个更大元素2.py
# @Time      :2024/07/20 16:40:51
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/next-greater-element-ii/

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dt = {}
        res = []
        maxn = max(nums)
        for i in range(len(nums)):
            if nums[i] == maxn:
                res.append(-1)
            else:
                if dt.get(nums[i])!=None:
                    res.append(dt.get(nums[i]))
                    continue
                for j in range(i+1,len(nums)):
                    if nums[j] > nums[i]:
                        dt[nums[i]] = nums[j]
                        res.append(nums[j])
                        break
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElements([1,2,3,4,3]))

