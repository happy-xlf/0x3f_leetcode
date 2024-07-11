class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        left=intervals[0][0]
        right=intervals[0][1]
        res=[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=right:
                right=max(right,intervals[i][1])
            else:
                res.append([left,right])
                left=intervals[i][0]
                right=intervals[i][1]
        res.append([left,right])
        return res



if __name__ == '__main__':
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge(intervals))
