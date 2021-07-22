# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
              
    
# Recursive approach    
#     def preorderTraversal(self, root):
#         s=[]
#         self.traversal(root,s)
#         return s
    
#     def traversal(self,root,s):
#         if root is None:
#             return
#         s.append(root.val)
#         self.traversal(root.left,s)
#         self.traversal(root.right,s)
        
        