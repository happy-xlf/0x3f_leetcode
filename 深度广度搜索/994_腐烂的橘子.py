#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   994_腐烂的橘子.py
@Time    :   2024/05/24 14:27:26
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def check(i,j):
            if grid[i][j] == 1:
                add = [(0,1), (0,-1), (1,0), (-1,0)]
                
                for item in add:
                    x = i + item[0]
                    y = j + item[1]
                    if x<0 and x>=n and y<0 and y>=m and grid[x][y]!=0:
                        return False
                return True
            else:
                return False
        cnt=0
        for i in range(n):
            cnt+=grid[i].count(1)
        if cnt==0:
            return 0
        for i in range(n):
            for j in range(m):
                if check(i,j):
                    return -1
                


if __name__ == '__main__':
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    s = Solution()
    print(s.orangesRotting(grid))
