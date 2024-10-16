#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   41_缺失的第一个正数.py
@Time    :   2024/10/14 11:48:49
@Author  :   Lifeng Xu 
@desc :   
'''
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        rang_n = len(nums) + 2
        for i in range(1, rang_n):
            if nums.count(i) == 0:
                return i

if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([1,2,0]))