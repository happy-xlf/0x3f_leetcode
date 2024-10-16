class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        for l in range(n):
            for i in range(n - l):
                j = i + l
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans
s = "babad"
print(Solution().longestPalindrome(s))