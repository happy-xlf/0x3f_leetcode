#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   56_合并区间.py
@Time    :   2024/10/13 15:00:46
@Author  :   Lifeng Xu 
@desc :   
'''
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        bg = intervals[0][0]
        ed = intervals[0][1]
        for interval in intervals:
            if interval[0] <= ed:
                ed = max(ed, interval[1])
            else:
                res.append([bg, ed])
                bg = interval[0]
                ed = interval[1]
        res.append([bg, ed])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,5],[0,4]]))
