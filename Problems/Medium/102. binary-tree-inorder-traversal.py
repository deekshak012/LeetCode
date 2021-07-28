# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        traversal, queue = [[root.val]], [root.left,root.right]
        level=1
        while(queue):
            temptraversal=[]
            for _ in xrange(len(queue)):
                temp = queue.pop(0)
                if temp:
                    temptraversal.append(temp.val)
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
            if temptraversal:
                traversal.append(temptraversal);
        return traversal