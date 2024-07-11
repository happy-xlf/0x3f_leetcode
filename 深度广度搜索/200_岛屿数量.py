#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   200_岛屿数量.py
@Time    :   2024/05/24 13:54:02
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        flag = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            add = [(0,1), (0,-1), (1,0), (-1,0)]
            flag[i][j] = True
            for item in add:
                x = i + item[0]
                y = j + item[1]
                if x>=0 and x<n and y>=0 and y<m and grid[x][y]=="1" and flag[x][y] == False:
                    dfs(x,y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and flag[i][j] == False:
                    dfs(i, j)
                    res+=1
        return res

if __name__ == '__main__':
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    s = Solution()
    print(s.numIslands(grid))
    

