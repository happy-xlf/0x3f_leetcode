#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   322_零钱兑换.py
@Time    :   2024/04/05 14:59:52
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for it in coins:
            for i in range(it, amount+1):
                dp[i] = min(dp[i], dp[i-it]+1)
        ans = dp[amount]
        return ans if ans != float("inf") else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    s = Solution()
    print(s.coinChange(coins, amount))

