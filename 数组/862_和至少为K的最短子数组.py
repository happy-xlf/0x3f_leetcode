#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :862_和至少为K的最短子数组.py
# @Time      :2024/08/06 10:31:31
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/
from typing import List
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
        d = deque()
        minx = 10000090
        for i in range(n + 1):
            while d and preSum[i] - preSum[d[0]] >= k:
                minx = min(minx, i - d.popleft())
            while d and preSum[i] <= preSum[d[-1]]:
                d.pop()
            d.append(i)
        return minx if minx != 10000090 else -1
            



if __name__ == "__main__":
    s = Solution()
    print(s.shortestSubarray([2,-1,2], 3))