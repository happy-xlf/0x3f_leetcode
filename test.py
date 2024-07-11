#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2024/05/20 17:37:04
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

# 给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

# 示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

def ans(s):
    tmp = []
    maxn = 0
    for it in s:
        while it in tmp:
            tmp.pop(0)
        tmp.append(it)
        maxn =max(maxn, len(tmp))
    
    return maxn

if __name__ == '__main__':
    sr = "abcabcbb"
    maxn = ans(sr)
    print(maxn)

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
        return matrix



