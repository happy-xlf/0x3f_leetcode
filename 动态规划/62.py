#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   62.py
@Time    :   2024/10/11 14:49:36
@Author  :   Lifeng Xu 
@desc :   
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    
