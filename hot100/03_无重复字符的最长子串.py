class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        r=0

        max_len=0
        dt={}
        while r<=len(s)-1:
            if s[r] not in dt:
                dt[s[r]]=1
                r+=1
            else:
                while l<r:
                    if s[l]==s[r]:
                        dt.pop(s[l])
                        l+=1
                        break
                    else:
                        dt.pop(s[l])
                        l+=1
            max_len=max(max_len,r-l)
        return max_len

if __name__ == '__main__':
    s=Solution()
    k="pwwkew"
    ans=s.lengthOfLongestSubstring(k)
    print(ans)