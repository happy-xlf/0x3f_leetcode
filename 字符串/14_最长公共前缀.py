#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   14_最长公共前缀.py
@Time    :   2024/04/02 15:35:00
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        min_j = min(len(t) for t in strs)
        
        res = ""
        if min_j == 0:
            return res
        
        for j in range(min_j):
            for i in range(len(strs)):
                if i == 0:
                    f=strs[i][j]
                else:
                    if f == strs[i][j]:
                        continue
                    else:
                        return res
            res+=f
        return res
                    


if __name__ == '__main__':
    strs = ["","","flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
