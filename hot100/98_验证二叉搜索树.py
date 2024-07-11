# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        
        def check(root,lower,upper):
            if not root:
                return True
            val=root.val
            if val<=lower or val>=upper:
                return False

            if not check(root.left,lower,val):
                return False

            if not check(root.right,val,upper):
                return False
            
            return True
        
        return check(root,float('-inf'),float('inf'))