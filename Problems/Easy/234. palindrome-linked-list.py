# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        l,r=head,head
        stack=[]
        while(r is not None):
            stack.append(r)
            r=r.next
        leng=len(stack)//2
        r=stack.pop()
        while(l!=r and len(stack)>=leng):
            if(l.val!=r.val):
                return False
            l=l.next
            r=stack.pop()
        return True
        
            
        