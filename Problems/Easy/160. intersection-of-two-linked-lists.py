# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):        
        curA=headA
        curB=headB
        times=3
        while(times):
            while(curA and curB):
                if(curA == curB):
                    return curA
                else:
                    curA=curA.next
                    curB=curB.next
            if(not curA and curB): curA=headB
            if(curA and not curB): curB=headA
            times-=1
        return None
    
#online submission(best solution)
# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         if headA and headB:
#             A, B = headA, headB
#         while A!=B:
#             A = A.next if A else headB
#             B = B.next if B else headA
#         return A
        
#Finding the length (my solution)
# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         if headA == headB:
#             return headA
#         curA=headA
#         lenA = 0
#         while(curA is not None):
#             lenA+=1
#             curA=curA.next
#         curB=headB
#         lenB = 0
#         while(curB is not None):
#             lenB+=1
#             curB=curB.next
#         if(lenA>lenB):
#             diff = lenA-lenB
#             while(diff is not 0):
#                 headA=headA.next
#                 diff-=1
#         elif(lenB>lenA):
#             diff = lenB-lenA
#             while(diff is not 0):
#                 headB=headB.next
#                 diff-=1
#         while(headA is not None or headB is not None):
#             if(headA == headB):
#                 return headA
#             headA=headA.next
#             headB=headB.next
#         return None
            