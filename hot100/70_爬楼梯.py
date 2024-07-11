class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0 for i in range(n+1)]
        dp[0]=1
        for i in range(n+1):
            dp[i]=dp[i-1]+dp[i-2] if i-2>=0 else 1
        return dp[n]





if __name__ == '__main__':
    solution=Solution()
    n=2
    print(solution.climbStairs(n))


