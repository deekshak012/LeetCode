# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    traversal.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return traversal
    
    
    
    
# Recursive approach    
#     def postorderTraversal(self, root):
#         s=[]
#         self.traversal(root,s)
#         return s
    
#     def traversal(self,root,s):
#         if root is None:
#             return
#         self.traversal(root.left,s)
#         self.traversal(root.right,s)
#         s.append(root.val)