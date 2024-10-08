#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1044_最长重复子串.py
# @Time      :2024/07/30 11:50:26
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/longest-duplicate-substring/
# 思路：
# 查找字符串中最长的重复子串
# 1、从左到右遍历字符串
# 2、利用左右指针截取字符串a
# 3、在左指针右侧的子字符串中查找是否存在字符串a
# 4、存在则可以增加截取字符串a的长度，即右指针向右移动一位
# 不存在则左指针向右移动一位

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        l,r =0,1 
        res = ""
        n = len(s)
        while r < n:
            if s[l:r] in s[l+1:]:
                if r - l > len(res):
                    res = s[l:r]
                r += 1
                continue
            l += 1
            if l == r:
                r += 1
        return res


if __name__ == "__main__":
    s = "banana"
    slution = Solution()
    print(slution.longestDupSubstring(s))