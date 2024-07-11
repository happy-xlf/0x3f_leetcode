class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dit={}
        for i in t:
            if i not in dit:
                dit[i]=1
            else:
                dit[i]+=1
        need=len(t)
        minl=""
        left=0
        right=0
        while right<len(s):
            if s[right] not in dit:
                right+=1
                continue
            dit[s[right]]-=1
            if dit[s[right]]>=0:
                need-=1
            while need==0:
                if minl=="":
                    minl=s[left:right+1]
                else:
                    if len(minl)>right-left+1:
                        minl=s[left:right+1]
                while left<right and s[left] not in dit:
                    left+=1
                dit[s[left]]+=1
                if dit[s[left]]<=0:
                    left+=1
                    continue
                need+=1
                if len(minl)>right-left+1:
                    minl=s[left:right+1]                
                left+=1
            else:
                right+=1

        return minl

if __name__ == '__main__':
    solution=Solution()
    s = "bdab"
    t = "ab"
    print(solution.minWindow(s, t))


