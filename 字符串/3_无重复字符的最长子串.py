#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   3_无重复字符的最长子串.py
@Time    :   2024/05/18 17:34:21
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxn = 0
        res = ""
        for it in s:
            while it in res:
                res=res[1:]
            res+=it
            maxn = max(maxn, len(res))
        return maxn






if __name__ == '__main__':
    s = "abcabcbb"
    so = Solution()
    print(so.lengthOfLongestSubstring(s))
