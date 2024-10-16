from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        st = {}
        dt = {}
        k = len(p)
        for it in p:
            dt[it] = dt.get(it, 0) + 1
        res = []
        for i in range(len(s)):
            if i==0:
                tmp = s[i:i+k]
                for it in tmp:
                    st[it] = st.get(it, 0) + 1
                if st == dt:
                    res.append(i)
            else:
                if i+k-1 < len(s):
                    st[s[i-1]] = st.get(s[i-1], 0) - 1
                    if st[s[i-1]] == 0:
                        del st[s[i-1]]
                    st[s[i+k-1]] = st.get(s[i+k-1], 0) + 1
                    if st == dt:
                        res.append(i)
                else:
                    break
        return res

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))