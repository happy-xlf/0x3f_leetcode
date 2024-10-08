#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :read_data.py
# @Time      :2024/07/30 14:15:56
# @Author    :Lifeng
# @Description :
import pandas as pd
import re
import json


# df = pd.read_excel('./output_crcLLMResponse_0726.xlsx')
# crcLLMResponse = df["crcLLMResponse"].values

# reason = []
# for it in crcLLMResponse:
#     # print(it)
#     it_json = json.loads(it)
    
#     pattern = re.compile(r'"reason": "(.*?)"')

#     # 搜索匹配
#     match = pattern.search(it_json)
#     if match:
#         # print(match.group(1))  # 输出：虚假宣传
#         reason.append(match.group(1))
#     else:
#         pattern = r"'reason': '(.*?)'"
#         match = re.search(pattern, it)
#         if match:
#             res = match.group(1)
#             res = res.split('\"')[0].replace("\\", "")
#             print(res)
#             reason.append(res)
#         else:
#             print("未找到reason值")

# df["reason"] = reason
# df.to_excel('./output_crcLLMResponse_0726_reason.xlsx', index=False)
import os
def get_all_path(dir_path):
    all_path = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            all_path.append(file_path)
    return all_path

print(get_all_path("./字符串/"))
