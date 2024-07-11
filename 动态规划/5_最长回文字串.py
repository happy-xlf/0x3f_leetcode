#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   5_最长回文字串.py
@Time    :   2024/04/02 15:15:23
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n==1:
            return s
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0
        for i in range(n-1,-1,-1):
            dp[i][i]=True
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j-i<=2:
                        dp[i][j]=True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] and j-i+1>max_len:
                        max_len = j-i+1
                        start = i
        return s[start:start+max_len]       


if __name__ == '__main__':
    s = "ac"
    solution = Solution()
    print(solution.longestPalindrome(s))
