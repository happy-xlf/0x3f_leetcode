#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1003_搜索旋转数组.py
# @Time      :2024/08/06 10:49:08
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/search-rotate-array-lcci/
from typing import List
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
          
            if arr[left] < arr[mid]:
                if arr[left] <= target <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif arr[left] > arr[mid]:
                if arr[left] <= target or target <= arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif arr[left] == arr[mid]:
                if arr[left] != target:
                    left += 1
                else:
                    right = left
        return left if arr[left] == target else -1                 # 返回left，或者-1



if __name__ == "__main__":
    s = Solution()
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    target = 5
    print(s.search(arr, target))