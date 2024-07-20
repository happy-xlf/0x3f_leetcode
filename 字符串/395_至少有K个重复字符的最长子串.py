#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :395_至少有K个重复字符的最长子串.py
# @Time      :2024/07/20 16:24:38
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/description/

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubstring("ababbc", 2))