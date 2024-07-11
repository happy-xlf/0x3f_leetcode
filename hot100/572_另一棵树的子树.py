#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :572_另一棵树的子树.py
# @Time      :2024/06/28 19:37:45
# @Author    :Lifeng
# @Description :
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return self.sameTree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def sameTree(self,s,t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.sameTree(s.left,t.left) and self.sameTree(s.right,t.right)