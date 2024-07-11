#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   70_爬楼梯.py
@Time    :   2024/04/02 11:06:29
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[n] = dp[n-1] + dp[n-2]
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
if __name__ == '__main__':
    s = Solution()
    n = int(input())
    print(s.climbStairs(n))
