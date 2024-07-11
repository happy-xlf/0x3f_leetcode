class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==0:
            return 0
        dp=[0]*n
        max_len=0
        for i in range(n):
            if i>0 and s[i]==')':
                if s[i-1]=='(':
                    dp[i]=dp[i-2]+2
                elif s[i-1]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                    j=i-dp[i-1]-2
                    dp[i]=dp[i-1]+2+dp[j]
                max_len=max(max_len,dp[i])
        return max_len

if __name__ == '__main__':
    solution = Solution()
    s="()(())"
    print(solution.longestValidParentheses(s))



