#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :977_有序数组的平方.py
# @Time      :2024/07/30 15:04:20
# @Author    :Lifeng
# @Description :
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            if nums[i]<0:
                new_list.insert(0,-nums[i])
            else:
                break
        if len(new_list) == len(nums):
            return [i**2 for i in new_list]
        res = []
        k = 0
        j = i
        while j < len(nums):
            if k < len(new_list):
                if nums[j] < new_list[k]:
                    res.append(nums[j]**2)
                    j+=1
                else:
                    res.append(new_list[k]**2)
                    k+=1
            else:
                res.append(nums[j]**2)
                j+=1
        while k < len(new_list):
            res.append(new_list[k]**2)
            k+=1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-2,0]))