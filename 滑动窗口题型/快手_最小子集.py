#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   快手_最小子集.py
@Time    :   2024/06/03 14:30:57
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
"""
# 有一个字符串s，含有m种字符，求该字符串中连续包含m种字符的最小子集长度。 s的长度 >> m

# s=“aabbccba” m= 3  output=3 “cba”


def min_length_of_sub(s, m):
    char_count = {}
    left = 0
    right = 0
    min_length = float("inf")

    while right < len(s):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) == m:
            if right - left + 1 < min_length:
                min_length = right - left + 1
            if s[left] in char_count:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

        right += 1
    return min_length


print(min_length_of_sub("aabbccba", 3))
