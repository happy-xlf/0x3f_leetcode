#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :09_回文数.py
# @Time      :2024/06/28 20:06:50
# @Author    :Lifeng
# @Description :
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
    

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))