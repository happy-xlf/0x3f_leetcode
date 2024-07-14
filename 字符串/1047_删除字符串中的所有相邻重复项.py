#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1047_删除字符串中的所有相邻重复项.py
# @Time      :2024/07/14 17:55:20
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/description/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        cur_list = []
        for it in s:
            if it not in cur_list:
                cur_list.append(it)
            else:
                if cur_list[-1] == it:
                    cur_list.pop()
                else:
                    cur_list.append(it)
        return "".join(cur_list)



if __name__ == "__main__":
    S = Solution()
    print(S.removeDuplicates("abbaca"))
