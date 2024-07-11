#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :287_寻找重复元素.py
# @Time      :2024/07/07 19:38:28
# @Author    :Lifeng
# @Description :
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums)
        res =-1
        while l<=r:
            mid = l+r>>1
            cnt = sum(1 for num in nums if num<=mid)
            if cnt<=mid:
                l = mid+1
            else:
                r = mid-1
                res = mid
        return res



if __name__ == "__main__":
    nums = [3,1,3,4,2]

    print(Solution().findDuplicate(nums))