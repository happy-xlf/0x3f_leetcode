class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dit={}
        res = 0
        l=0
        for r,x in enumerate(s):
            dit[x]=dit.get(x,0)+1
            while dit[x] > 1:
                dit[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res


if __name__ == '__main__':
    s = input("s:")
    solve= Solution()
    print(solve.lengthOfLongestSubstring(s))