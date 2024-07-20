#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :96_交错字符串.py
# @Time      :2024/07/20 11:54:13
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/IY6buf/
# 动态规划
# dp[i][j] 表示 s1[0:i] 和 s2[0:j] 是否可以交错组成 s3[0:i+j]
# 状态转移方程：dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
# 初始条件：dp[0][0] = True
# 时间复杂度：O(mn)，空间复杂度：O(mn)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        for i in range(1, n1 + 1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n2 + 1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[n1][n2]
    
if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(Solution().isInterleave(s1, s2, s3))