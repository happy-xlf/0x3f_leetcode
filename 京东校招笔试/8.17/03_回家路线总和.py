#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :03_回家路线总和.py
# @Time      :2024/08/17 12:02:42
# @Author    :Lifeng
# @Description :
import sys

n,m,a = map(int, input().split())
road = [[[]] * 100 for _ in range(100)]
for i in range(m):
    u,v,w = map(int, input().split())
    road[v][u].append(w)

res = []
def dfs(road, a, index , num):
    if index == 1 and a == 0:
        res.append(num)
    cost_list = road[index][index-1]
    for cost in cost_list:
        dfs(road, a-cost, index-1, num)
dfs(road, a, n, 1)
print(res)
print(sum(res))