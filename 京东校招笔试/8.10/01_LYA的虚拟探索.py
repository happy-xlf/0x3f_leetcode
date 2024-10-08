#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :01_LYA的虚拟探索.py
# @Time      :2024/08/16 23:13:21
# @Author    :Lifeng
# @Description :
import sys

instruction = map(str, input())
x,y = 0, 0
dx, dy = 0, 1
for it in instruction:
    if it == "W":
        x+= dx
        y += dy
    elif it =="A":
        dx, dy = -dy, dx
    elif it == "D":
        dx, dy = dy, -dx
print(x, y)