# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return head
        start = ListNode(None)
        start.next = head
        
        prev = start
        cur = head
        while(cur):
            if(cur.val==val):
                prev.next=cur.next
            else:
                prev=prev.next
            cur=cur.next
        return start.next
    
#Recursive solution
#      def removeElements(self, head: ListNode, val: int) -> ListNode:

#         if not head:
#             return head

#         head.next = self.removeElements(head.next, val)        
#         if head.val == val:
#             head = head.next

#         return head
        