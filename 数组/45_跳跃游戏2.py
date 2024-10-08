#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :45_跳跃游戏2.py
# @Time      :2024/07/30 15:24:13
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/jump-game-ii/description/
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        cur = 0
        next = 0
        for i in range(len(nums)):
            next = max(next, i + nums[i])
            if i == cur:
                if cur != len(nums) - 1:
                    res += 1
                    cur = next
                    if next >= len(nums) - 1:
                        break
                else:
                    break
        return res
    

    def jump2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        cur = 0
        next = 0
        for i in range(len(nums)-1):
            next = max(next, i + nums[i])
            if i == cur:
                res += 1
                cur = next
        return res



if __name__ == "__main__":
    s = Solution()
    print(s.jump2([2,3,1,1,4]))

