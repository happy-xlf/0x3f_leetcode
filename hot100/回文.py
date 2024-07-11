

# s="223889943"
# maxn=0
# ans=""
# #最长回文子串


# for i in range(len(s)):
#     for j in range(i):
#         if s[i:j]==s[j:i]:
#             if j-1+1>maxn:
#                 maxn=j-i+1
#                 ans=s[i:j]

# "511211"
# "abcdeeee"
# left=0
# right=len(s)-1

# k=0
# while left<right:
#     if s[left:right]==s[right:left]:
#         ans = s[left:right]
#         break
#     if k==0:
#         left+=1
#         k=1
#     else:
#         right-=1
#         k=0

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n<2:
            return s

        dp=[[False] *len(s) for _ in range(len(s))]

        start,max_len=0,1
        for r in range(1,len(s)):
            for l in range(r):
                if r-l<=2:
                    if s[l]==s[r]:
                        dp[l][r] = True
                        cur_len=r-l+1
                else:
                    if s[l]==s[r] and dp[l+1][r-1]:
                        dp[l][r] = True
                        cur_len = r-l+1
                

                if dp[l][r] and cur_len > max_len:
                    max_len=cur_len
                    start=l

        return s[start:start+max_len]




if __name__ == '__main__':
    solution =Solution()
    s="babad"
    print(solution.longestPalindrome(s))
























