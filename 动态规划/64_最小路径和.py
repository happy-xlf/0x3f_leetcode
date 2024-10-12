from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            if i>0:
                dp[i][0] += dp[i-1][0] + grid[i][0]
            else:
                dp[i][0] = grid[i][0]
        
        for j in range(m):
            if j>0:
                dp[0][j] += dp[0][j-1] + grid[0][j]
            else:
                dp[0][j] = grid[0][j]
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]