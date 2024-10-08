#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :560_和为K的子数组.py
# @Time      :2024/08/19 23:23:31
# @Author    :Lifeng
# @Description :
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        presums={0:1}

        sum=0
        for i in range(n):
            sum+=nums[i]
            count+=presums.get(sum-k,0)
            presums[sum]=presums.get(sum,0)+1
        return count

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    k = 3
    print(s.subarraySum(nums, k))