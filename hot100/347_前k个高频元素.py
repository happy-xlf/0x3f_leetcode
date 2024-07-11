#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :347_前k个高频元素.py
# @Time      :2024/07/07 19:27:11
# @Author    :Lifeng
# @Description :
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dit = {}
        for it in nums:
            dit[it]=dit.get(it,0)+1
        ans=sorted(dit.items(),key=lambda x:x[1],reverse=True)
        res=[]
        i=0
        for key,value in ans:
            res.append(key)
            i+=1
            if i==k:
                break
        return res