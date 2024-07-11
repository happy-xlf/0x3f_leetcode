#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   746_使用最小花费爬楼梯.py
@Time    :   2024/04/02 11:14:07
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp[i] = min(dp[i-1], dp[i-2] + cost[i])
        dp = [0] * (len(cost)+1)
        if len(cost)<=2:
            return min(cost)
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+ cost[i-2])
        return dp[-1]
    
if __name__ == '__main__':
    s = Solution()
    cost =[int(k) for k in input().split()]
    print(s.minCostClimbingStairs(cost))
