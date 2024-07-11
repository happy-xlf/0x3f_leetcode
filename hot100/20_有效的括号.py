class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans=[]
        for t in s:
            if t=='(':
                ans.append(')')
            elif t=='[':
                ans.append(']')
            elif t=='{':
                ans.append('}')
            else:
                if len(ans)==0 or t!=ans.pop():
                    return False
        if len(ans)!=0:
            return False
        return True


if __name__ == '__main__':
    s = "()[]"
    solution = Solution()
    print(solution.isValid(s))
