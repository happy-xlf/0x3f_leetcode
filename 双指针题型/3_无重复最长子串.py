class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = []
        maxn = 0
        for i in range(len(s)):
            if s[i] not in mp:
                mp.append(s[i])
            else:
                maxn = max(maxn, len(mp))
                while s[i] in mp:
                    mp.pop(0)
                mp.append(s[i])
        maxn = max(maxn, len(mp))
        return maxn
                