#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :670_最大交换.py
# @Time      :2024/07/24 10:03:24
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/maximum-swap/description/

class Solution:
    def maximumSwap(self, num: int) -> int:
        # 最大交换,至多交换一次数字中的任意两位，返回最大值
        s = list(str(num))
        
        change = [-1] * len(s)
        change[-1] = len(s)-1
        for i in range(len(s)-2, -1, -1):
            if s[i] <= s[i+1] or s[i] <= s[change[i+1]]:
                change[i] = change[i+1]
            else:
                change[i] = i
      
        for i in range(len(s)):
            if change[i] != i and s[i] != s[change[i]]:
                s[i], s[change[i]] = s[change[i]], s[i]
                return int("".join(s))
        return num
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSwap(num=1993)) # 7236




