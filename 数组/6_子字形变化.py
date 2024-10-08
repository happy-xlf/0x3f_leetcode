#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :6_子字形变化.py
# @Time      :2024/08/04 17:26:47
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ""
        if numRows == 1:
            return s
        result = [""]*numRows
        i=0
        n=len(s)
        while i<n:
            for j in range(numRows):
                if i<n:
                    result[j] += s[i]
                    i+=1
            for j in range(numRows-2,0,-1):
                if i<n:
                    result[j] += s[i]
                    i+=1
        return "".join(result)
    
if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))