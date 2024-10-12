#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   55_跳跃游戏.py
@Time    :   2024/10/11 17:48:21
@Author  :   Lifeng Xu 
@desc :   
'''
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True