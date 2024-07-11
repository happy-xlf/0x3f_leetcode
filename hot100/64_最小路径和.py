class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp=[[0]*len(grid[0]) for i in range(len(grid))]
        dp[0][0]=grid[0][0]
        for i in range(1,len(grid[0])):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        for i in range(1,len(grid)):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(dp[i][j])
        return dp[-1][-1]





if __name__ == '__main__':
    solution=Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]

    print(solution.minPathSum(grid))


