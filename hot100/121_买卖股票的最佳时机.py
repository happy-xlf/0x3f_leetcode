class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_num = float('inf')
        max_num = 0
        for price in prices:
            min_num=min(min_num,price)
            max_num=max(max_num,price - min_num)
        return max_num




if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))



