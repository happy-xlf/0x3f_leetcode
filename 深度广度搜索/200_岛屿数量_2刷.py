#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :200_岛屿数量_2刷.py
# @Time      :2024/08/13 12:04:20
# @Author    :Lifeng
# @Description :
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        check = [[False] * len(grid[0]) for _ in range(len(grid))]
        res = 0
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1" or check[i][j]:
                return
            check[i][j] = True
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not check[i][j]:
                    dfs(i, j)
                    res += 1
        return res


if __name__ == "__main__":
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    print(Solution().numIslands(grid))