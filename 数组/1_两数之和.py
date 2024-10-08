#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1_两数之和.py
# @Time      :2024/08/19 22:58:04
# @Author    :Lifeng
# @Description :
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            if target - nums[i] in nums[i+1:]:
                k = nums.index(target - nums[i])
                if k != i:
                    return [i, k]

        
if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 4]
    target = 6
    print(s.twoSum(nums, target))