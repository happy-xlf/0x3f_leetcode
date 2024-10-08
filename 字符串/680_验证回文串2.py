#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :680_验证回文串2.py
# @Time      :2024/08/06 10:38:44
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s, i, j, flag):
            while i < j:
                if s[i] != s[j]:
                    if flag:
                        return check(s, i+1, j, False) or check(s, i, j-1, False)
                    else:
                        return False
                i += 1
                j -= 1
            return True

        return check(s, 0, len(s)-1, True)



if __name__ == "__main__":
    s = Solution()
    print(s.validPalindrome("1235"))