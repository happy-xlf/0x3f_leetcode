#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :264_丑数2.py
# @Time      :2024/07/20 14:55:54
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/ugly-number-ii/
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1] * n
        n2, n3, n5 = 0, 0, 0
        for i in range(1, n):
            res[i] = min(res[n2] * 2, res[n3] * 3, res[n5] * 5)
            if res[i] == res[n2] * 2: n2 += 1
            if res[i] == res[n3] * 3: n3 += 1
            if res[i] == res[n5] * 5: n5 += 1
        return res[-1]
    
if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(100))
