#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :103_零钱兑换.py
# @Time      :2024/08/13 17:30:53
# @Author    :Lifeng
# @Description :
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for con in coins:
            for i in range(con,amount+1):
                dp[i]=min(dp[i],dp[i-con]+1)
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]
    
if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))