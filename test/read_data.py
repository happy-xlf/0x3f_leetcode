#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :read_data.py
# @Time      :2024/08/05 11:16:40
# @Author    :Lifeng
# @Description :
import json


res = []
with open("./pred_10.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        res.append(data)

print(res)