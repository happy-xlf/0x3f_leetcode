#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :6678_有效的括号字符串.py
# @Time      :2024/07/14 17:21:59
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/valid-parenthesis-string/description/

class Solution:
    def checkValidString(self, s: str) -> bool:
        minx = 0
        maxx = 0
        for i in range(len(s)):
            if s[i] == '(':
                minx += 1
                maxx += 1
            elif s[i] == ')':
                minx -= 1
                maxx -= 1
            elif s[i] == '*':
                minx -= 1
                maxx += 1
            if minx<0:
                minx += 1
            if maxx < 0:
                return False
        return minx == 0
            



if __name__ == "__main__":
    s = Solution()
    print(s.checkValidString("(((*)"))

