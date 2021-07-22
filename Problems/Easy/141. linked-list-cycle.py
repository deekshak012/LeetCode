# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None: return False
        cur=head;
        curtwo=head.next;
        while(cur is not None and curtwo is not None):
            if cur == curtwo:
                return True
            if curtwo.next is None :
                return False
            cur = cur.next
            curtwo = curtwo.next.next
        return False