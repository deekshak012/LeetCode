# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        if(not root):
            return []
        result, stack = [],  [(root,"")]
        while(stack):
            node, ls = stack.pop()
            if(node.left is None and node.right is None):
                result.append(ls+str(node.val))
            if(node.right):
                stack.append((node.right,ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return result
            
        