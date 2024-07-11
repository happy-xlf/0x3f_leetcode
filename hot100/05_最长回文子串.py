class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""

        for i in range(len(s)):
            star=max(0,i-len(res)-1)
            temp=s[star:i+1]
            if temp==temp[::-1]:
                res=temp
            else:
                temp=temp[1:]
                if temp==temp[::-1]:
                    res=temp
        
        return res
    
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=len(s)
        if l==1:
            return s
        dp=[[False] * l for _ in range(l)]
        max_len=1
        start=0
        cur_len=0
        for j in range(1,l):
            for i in range(j):
                if j-i<=2:
                    if s[i]==s[j]:
                        dp[i][j]=True
                        cur_len=j-i+1
                else:
                    if s[i]==s[j] and dp[i+1][j-1]:
                        dp[i][j]=True
                        cur_len=j-i+1
                if cur_len>max_len:
                    max_len=cur_len
                    start=i
        return s[start:start+max_len]
    
    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n<2:
            return s
        start,max_len=0,1
        dp=[[False] * n for _ in range(n)]

        for r in range(n):
            for l in range(r+1):
                cur_len=r-l+1
                if cur_len==1:
                    dp[l][r]=True
                elif cur_len==2:
                    dp[l][r]= s[l]==s[r]
                else:
                    dp[l][r]= dp[l+1][r-1] and s[l]==s[r]

                if dp[l][r] and cur_len>max_len:
                    max_len=cur_len
                    start=l
        return s[start:start+max_len]





if __name__ == '__main__':
    s = "babad"
    s = "abba"
    solution = Solution()
    result = solution.longestPalindrome3(s)
    print(result)




