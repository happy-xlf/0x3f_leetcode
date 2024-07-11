class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)

        ans=[]

        def dfs(candidates, target, path, res, start):
            if res==target:
                ans.append(path)
                return
            if res>target:
                return
            else:
                for i in range(start,len(candidates)):
                    if res+candidates[i]<=target:
                        dfs(candidates, target, path+[candidates[i]], res+candidates[i], i)
        dfs(candidates, target, [], 0, 0)
        return ans

if __name__ == '__main__':
    solution = Solution()
    candidates = [2]
    target = 1
    print(solution.combinationSum(candidates, target))


