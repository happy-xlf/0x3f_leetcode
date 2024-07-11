# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        queue=[]
        queue.append(root)
        res=[]
        
        while queue:
            size=len(queue)
            nums=[]
            for _ in range(size):
                cur=queue.pop(0)
                if not cur:
                    continue
                nums.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if nums:
                res.append(nums)
        return res
            