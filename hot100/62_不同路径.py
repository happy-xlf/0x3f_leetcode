class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0]=1
        for i in range(n):
            dp[0][i]=1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]



if __name__ == '__main__':
    solution = Solution()
    m = 3
    n = 7
    print(solution.uniquePaths(m, n))
